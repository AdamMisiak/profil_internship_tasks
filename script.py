import django
import json
import argparse
from django.apps import apps
from datetime import date, datetime
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'profil_intern.settings'
django.setup()
Person = apps.get_model('queries', 'Person')


def calculate_how_many_days_to_birthday(dob, age):
	today = date.today()
	dob = dob[:10].replace('-', '/')
	date_of_birthday = datetime.strptime(dob, '%Y/%m/%d').date()
	date_of_birthday_this_year = date_of_birthday.replace(year=date_of_birthday.year+age)
	days_to_birthday = (date_of_birthday_this_year - today).days
	if days_to_birthday < 0:
		if (date_of_birthday_this_year.year + 1) % 4 == 0:
			days_to_birthday = days_to_birthday + 366
		else:
			days_to_birthday = days_to_birthday + 365
	return days_to_birthday


def create_database():
	with open('queries/persons.json') as file:
		data = json.load(file)
	print('Please wait, database is creating...')
	data = data['results']
	for person in data:
		person = Person(gender=person['gender'], title=person['name']['title'], first=person['name']['first'],
			last=person['name']['last'], street_number=person['location']['street']['number'],
			street_name=person['location']['street']['name'], city=person['location']['city'],
			state=person['location']['state'], country=person['location']['country'],
			postcode=person['location']['postcode'], latitude=person['location']['coordinates']['latitude'],
			longitude=person['location']['coordinates']['latitude'],
			timezone_offset=person['location']['timezone']['offset'],
			timezone_description=person['location']['timezone']['description'], email=person['email'],
			login_uuid=person['login']['uuid'], username=person['login']['username'],
			password=person['login']['password'], password_salt=person['login']['salt'],
			password_md5=person['login']['md5'], password_sha1=person['login']['sha1'],
			password_sha256=person['login']['sha256'], dob=person['dob']['date'],
			age=person['dob']['age'], registered_date=person['registered']['date'],
			days_to_birthday=calculate_how_many_days_to_birthday(person['dob']['date'],person['dob']['age']),
			registered_age=person['registered']['age'],
			phone=person['phone'].replace('-', '').replace(' ', '').replace('(', '').replace(')', ''),
			cell=person['cell'].replace('-', '').replace(' ', '').replace('(', '').replace(')', ''),
			id_name=person['id']['name'], id_value=person['id']['value'],
			thumbnail=person['picture']['thumbnail'], nat=person['nat'])
		person.save()


def calculate_male_female_percentage():
	female = Person.objects.filter(gender='female').count()
	male = Person.objects.filter(gender='male').count()
	percentage_f = (female/(male+female))*100
	percentage_m = (male/(male+female))*100
	result = f"In database, there are {percentage_f}% women and {percentage_m}% men"
	return result


def calculate_average_age(sex):
	all_entries = Person.objects.all()
	age_list = [person.age for person in all_entries]
	age_list_male = [person.age for person in all_entries if person.gender == 'male']
	age_list_female = [person.age for person in all_entries if person.gender == 'female']

	age_sum = sum(age_list)
	age_sum_male = sum(age_list_male)
	age_sum_female = sum(age_list_female)

	people_counter = len(age_list)
	male_counter = len(age_list_male)
	female_counter = len(age_list_female)

	average_all = round(age_sum / people_counter,2)
	average_male = round(age_sum_male / male_counter,2)
	average_female = round(age_sum_female / female_counter,2)

	if sex == 'male':
		result = f'Average age for men is {average_male} years'
	elif sex == 'female':
		result = f'Average age for women is {average_female} years'
	elif sex == 'all':
		result = f'Average age for all is {average_all} years'
	else:
		result = 'Wrong argument! Please type: male, female or all'
	return result


def find_most_common_cities(elements):
	unique_cities={}
	all_entries = Person.objects.all()
	if elements.isnumeric():
		for person in all_entries:
			if person.city in unique_cities:
				unique_cities[person.city]=unique_cities[person.city]+1
			else:
				unique_cities[person.city]=1
		sorted_unique_cities = sorted(unique_cities.items(), key=lambda x: x[1], reverse=True)

		for city in sorted_unique_cities[:int(elements)]:
			print(city[0], city[1])
	else:
		print(f'{elements} is not a number! Inputs needs to be int type.')


def find_most_common_passwords(elements):
	unique_pass={}
	all_entries = Person.objects.all()
	if elements.isnumeric():
		for person in all_entries:
			if person.password in unique_pass:
				unique_pass[person.password]=unique_pass[person.password]+1
			else:
				unique_pass[person.password]=1
		sorted_unique_pass = sorted(unique_pass.items(), key=lambda x: x[1], reverse=True)

		for password in sorted_unique_pass[:int(elements)]:
			print(password[0], password[1])
	else:
		print(f'{elements} is not a number! Inputs needs to be int type.')


def find_birthdays_between_dates(start_date, end_date):
	all_entries = Person.objects.all()
	start_date_conv = datetime.strptime(start_date, '%Y/%m/%d').date()
	end_date_conv = datetime.strptime(end_date, '%Y/%m/%d').date()
	print(f'List of people with birthday between {start_date_conv} and {end_date_conv}:')
	for number, person in enumerate(all_entries):
		dob = datetime.strptime(person.dob[: 10].replace('-', '/'), '%Y/%m/%d').date()
		if start_date_conv < dob < end_date_conv:
			print(f'Person "{person.first} {person.last}" has birthday on: {dob}')


def calculate_safety_of_password():
	all_entries = Person.objects.all()
	pointed_pass={}
	for person in all_entries:
		is_lower_flag=False
		is_upper_flag=False
		is_numeric_flag=False
		is_special_flag=False
		pointed_pass[person.password] = 0
		if len(person.password) >= 8:
			pointed_pass[person.password] += 5
		for letter in person.password:
			if letter.islower() and not is_lower_flag:
				pointed_pass[person.password] += 1
				is_lower_flag = True

			if letter.isupper() and not is_upper_flag:
				pointed_pass[person.password] += 2
				is_upper_flag = True

			if letter.isnumeric() and not is_numeric_flag:
				pointed_pass[person.password] += 1
				is_numeric_flag = True

			if not letter.isalnum() and not is_special_flag:
				pointed_pass[person.password] += 3
				is_special_flag = True

	sorted_passwords = sorted(pointed_pass.items(), key=lambda x: x[1], reverse=True)
	for password in sorted_passwords:
		print(f'Password "{password[0]}" scores {password[1]} points for security')


my_parser = argparse.ArgumentParser()
my_parser.add_argument('task', action='store')
my_parser.add_argument('--arg', required=False)
my_parser.add_argument('--start', required=False)
my_parser.add_argument('--end', required=False)

args = my_parser.parse_args()

if args.task == 'male-female-percentage':
	print(calculate_male_female_percentage())
elif args.task == 'average-age':
	print(calculate_average_age(args.arg))
elif args.task == 'most-common-cities':
	find_most_common_cities(args.arg)
elif args.task == 'most-common-passwords':
	find_most_common_passwords(args.arg)
elif args.task == 'dob-between':
	find_birthdays_between_dates(args.start, args.end)
elif args.task == 'safety-of-passwords':
	calculate_safety_of_password()
elif args.task == 'create-db':
	create_database()
else:
	print('There is no such command! Check README.md file for available commands')


#query_5('1950/06/06','1963/10/05')
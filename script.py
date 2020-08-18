import django
import argparse
import requests
from django.apps import apps
from datetime import date, datetime
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'profil_intern.settings'
django.setup()
Person = apps.get_model('queries', 'Person')


class Database():
	def __init__(self, seed, number):
		self.seed = seed
		self.number = number

	def __str__(self):
		return str(f'Database created from {self.seed} seed, has {Person.objects.all().count()} records')

	def calculate_how_many_days_to_birthday(self, dob):
		today = date.today()
		dob = dob[:10].replace('-', '/')
		date_of_birthday = datetime.strptime(dob, '%Y/%m/%d').date()
		age = today.year - date_of_birthday.year
		date_of_birthday_this_year = date_of_birthday.replace(year=date_of_birthday.year + age)
		days_to_birthday = (date_of_birthday_this_year - today).days
		if days_to_birthday < 0:
			if (date_of_birthday_this_year.year + 1) % 4 == 0:
				days_to_birthday = days_to_birthday + 366
			else:
				days_to_birthday = days_to_birthday + 365
		return days_to_birthday

	def create_database(self):
		print('Please wait, database is creating...')
		people_json = requests.get(
			'https://randomuser.me/api/'
			+ '?results='
			+ str(self.number)
			+ '&seed='
			+ str(self.seed)).json()['results']

		for number, person in enumerate(people_json):
			person_record = Person(
				gender=person['gender'], title=person['name']['title'],
				first=person['name']['first'], last=person['name']['last'],
				street_number=person['location']['street']['number'],
				street_name=person['location']['street']['name'], city=person['location']['city'],
				state=person['location']['state'], country=person['location']['country'],
				postcode=person['location']['postcode'],
				latitude=person['location']['coordinates']['latitude'],
				longitude=person['location']['coordinates']['latitude'],
				timezone_offset=person['location']['timezone']['offset'],
				timezone_description=person['location']['timezone']['description'], email=person['email'],
				login_uuid=person['login']['uuid'], username=person['login']['username'],
				password=person['login']['password'], password_salt=person['login']['salt'],
				password_md5=person['login']['md5'], password_sha1=person['login']['sha1'],
				password_sha256=person['login']['sha256'], dob=person['dob']['date'],
				age=person['dob']['age'], registered_date=person['registered']['date'],
				days_to_birthday=self.calculate_how_many_days_to_birthday(person['dob']['date']),
				registered_age=person['registered']['age'],
				phone=person['phone'].replace('-', '').replace(' ', '').replace('(', '').replace(')', ''),
				cell=person['cell'].replace('-', '').replace(' ', '').replace('(', '').replace(')', ''),
				id_name=person['id']['name'], id_value=person['id']['value'],
				thumbnail=person['picture']['thumbnail'], nat=person['nat'])
			person_record.save()
			print(f'user number {number} has been created!')

	def calculate_male_female_percentage(self):
		female_counter = Person.objects.filter(gender='female').count()
		male_counter = Person.objects.filter(gender='male').count()
		percentage_f = round((female_counter / (male_counter + female_counter)) * 100, 3)
		percentage_m = round((male_counter / (male_counter + female_counter)) * 100, 3)
		result = f"In database, there are {percentage_f}% women and {percentage_m}% men"
		return result

	def calculate_average_age(self, sex):
		all_people = Person.objects.all()
		age_list = [person.age for person in all_people]
		age_list_male = [person.age for person in all_people if person.gender == 'male']
		age_list_female = [person.age for person in all_people if person.gender == 'female']

		age_sum = sum(age_list)
		age_sum_male = sum(age_list_male)
		age_sum_female = sum(age_list_female)

		people_counter = len(age_list)
		male_counter = len(age_list_male)
		female_counter = len(age_list_female)

		average_all = round(age_sum / people_counter, 2)
		average_male = round(age_sum_male / male_counter, 2)
		average_female = round(age_sum_female / female_counter, 2)

		if sex == 'male':
			result = f'Average age for men is {average_male} years'
		elif sex == 'female':
			result = f'Average age for women is {average_female} years'
		elif sex == 'all':
			result = f'Average age for all is {average_all} years'
		else:
			result = 'Wrong argument! Please type: male, female or all'
		return result

	def find_most_common_elements(self, searching_element_input, quantity='5'):
		all_people = Person.objects.all()
		if quantity.isnumeric():
			unique_elements = {}
			for person in all_people:
				if searching_element_input == 'city':
					searching_element = person.city
				elif searching_element_input == 'password':
					searching_element = person.password

				if searching_element in unique_elements:
					unique_elements[searching_element] = unique_elements[searching_element] + 1
				else:
					unique_elements[searching_element] = 1
			sorted_unique_elements = sorted(unique_elements.items(), key=lambda x: x[1], reverse=True)
			sorted_unique_elements = sorted_unique_elements[:int(quantity)]
			if int(quantity) > all_people.count():
				return f'{quantity} is too big! In database there are only {all_people.count()} people.'
			return sorted_unique_elements
		else:
			return f'{quantity} is not a number! Input needs to be int type.'

	def find_birthdays_between_dates(self, start_date, end_date):
		all_people = Person.objects.all()
		result_dict = {}
		try:
			start_date_conv = datetime.strptime(start_date, '%Y/%m/%d').date()
			end_date_conv = datetime.strptime(end_date, '%Y/%m/%d').date()
		except ValueError:
			return 'Date format needs to be YYYY/mm/dd (for example 2137/05/04)!'
		if (end_date_conv - start_date_conv).days < 0:
			return f'First date needs to be earlier then second one!'
		for person in all_people:
			dob = datetime.strptime(person.dob[: 10].replace('-', '/'), '%Y/%m/%d').date()
			if start_date_conv < dob < end_date_conv:
				result_dict[person.first + ' ' + person.last] = dob
		return result_dict

	def calculate_safety_points_of_password(self, password):
		is_lower_flag = False
		is_upper_flag = False
		is_numeric_flag = False
		is_special_flag = False
		points = 0
		if len(password) >= 8:
			points += 5
		for letter in password:
			if letter.islower() and not is_lower_flag:
				points += 1
				is_lower_flag = True

			if letter.isupper() and not is_upper_flag:
				points += 2
				is_upper_flag = True

			if letter.isnumeric() and not is_numeric_flag:
				points += 1
				is_numeric_flag = True

			if not letter.isalnum() and not is_special_flag:
				points += 3
				is_special_flag = True
		return password, points

	def check_people_passwords(self):
		all_people = Person.objects.all()
		pointed_passwords = {}
		for person in all_people:
			password, points = self.calculate_safety_points_of_password(person.password)
			pointed_passwords[password] = points
		sorted_passwords = sorted(pointed_passwords.items(), key=lambda x: x[1], reverse=True)
		return sorted_passwords


if __name__ == '__main__':
	# SEED FOR SAME RECORDS EVERY TIME
	seed = 'ec14fa7f0b8242e0'
	DB = Database(seed, 1000)
	my_parser = argparse.ArgumentParser()
	my_parser.add_argument('task', action='store')
	my_parser.add_argument('--arg', required=False)
	my_parser.add_argument('--start', required=False)
	my_parser.add_argument('--end', required=False)
	args = my_parser.parse_args()

	if args.task == 'male-female-percentage':
		print(DB.calculate_male_female_percentage())
	elif args.task == 'average-age':
		print(DB.calculate_average_age(args.arg))
	elif args.task == 'most-common-cities':
		try:
			result_cities = DB.find_most_common_elements('city', args.arg)
			for element in result_cities:
				print(element[0], element[1])
		except:
			print(DB.find_most_common_elements('city', args.arg))

	elif args.task == 'most-common-passwords':
		try:
			result_passwords = DB.find_most_common_elements('password', args.arg)
			for element in result_passwords:
				print(element[0], element[1])
		except:
			print(DB.find_most_common_elements('password', args.arg))

	elif args.task == 'dob-between':
		try:
			result_dates = DB.find_birthdays_between_dates(args.start, args.end)
			for element in result_dates.items():
				print(element[0], element[1])
		except:
			print(DB.find_birthdays_between_dates(args.start, args.end))

	elif args.task == 'safety-of-passwords':
		result_passwords = DB.check_people_passwords()
		for element in result_passwords:
			print(element[0], element[1])

	elif args.task == 'create-db':
		DB.create_database()
	else:
		print('There is no such command! Check README.md file for available commands')

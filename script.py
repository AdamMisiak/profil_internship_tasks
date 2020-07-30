import django
import json
from django.apps import apps
from datetime import date, datetime
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'profil_intern.settings'
django.setup()
Person = apps.get_model('queries', 'Person')


def calculate_how_many_days_to_birthday(dob, age):
	#needs to be checked with before/after Feb date
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

	data = data['results']
	for person in data:

		dob = calculate_how_many_days_to_birthday(person['dob']['date'],person['dob']['age'])
		print(dob)

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


def query_1():
	female = Person.objects.filter(gender='female').count()
	male = Person.objects.filter(gender='male').count()
	procentage_f = (female/(male+female))*100
	procentage_m = (male/(male+female))*100
	result = f"In database there are {procentage_f}% women and {procentage_m}% men"
	return result


def query_2():
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

	result = f'Whole database average age was {average_all} years, only female average age was {average_female} years' \
			 f'and only male average age was {average_male} years'
	return result


def query_3(elements):
	unique_cities={}
	all_entries = Person.objects.all()
	for person in all_entries:
		if person.city in unique_cities:
			unique_cities[person.city]=unique_cities[person.city]+1
		else:
			unique_cities[person.city]=1
	sorted_unique_cities = sorted(unique_cities.items(), key=lambda x: x[1], reverse=True)

	for city in sorted_unique_cities[:elements]:
		print(city[0], city[1])


query_3(6)
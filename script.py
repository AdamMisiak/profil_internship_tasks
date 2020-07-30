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


def script():
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


script()
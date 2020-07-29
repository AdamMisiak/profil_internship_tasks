import django
import json
from django.apps import apps
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'profil_intern.settings'
django.setup()

Person = apps.get_model('queries', 'Person')

def script():
	with open('queries/persons.json') as file:
		data = json.load(file)

	data = data['results']
	for person in data:

		print(person['gender'])
		person = Person(gender=person['gender'])
		person.save()


script()
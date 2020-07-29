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


		print((person['location']['city']))
		# person = Person(gender=person['gender'], title=person['name']['title'], first=person['name']['first'],
		# 	last=person['name']['last'], street_number=person['location']['street']['number'],
	# 		street_name=person['location']['street']['name'], city=person['location']['city'],
# 			state=person['location']['city']	)
		# person.save()


script()
import pytest
import unittest
import json
from script import Database


class TestDataBase(unittest.TestCase):
	def test_database(self):
		with open('persons.json') as file:
			data = json.load(file)
		DB = Database(data)
		random_person = "{'gender': 'male', 'name': {'title': 'Mr', 'first': 'Eeli', 'last': 'Lehtonen'}, " \
						"'location': {'street': {'number': 4609, 'name': 'Pyynikintie'}, 'city': 'Ruokolahti'," \
						" 'state': 'Kainuu', 'country': 'Finland', 'postcode': 22940, " \
						"'coordinates': {'latitude': '36.3772', 'longitude': '-168.6461'}," \
						" 'timezone': {'offset': '-2:00', 'description': 'Mid-Atlantic'}}," \
						" 'email': 'eeli.lehtonen@example.com', 'login': {'uuid': '580e2650-e197-412c-a1ea-175bb58bf78e'," \
						" 'username': 'smallrabbit241', 'password': 'baylor', " \
						"'salt': 'LZRcNjIr', 'md5': '4f0281a696b76156c592edac7f19250a', " \
						"'sha1': '77f943e665bd331d92eef4fb17a9acabf948223e', " \
						"'sha256': '21d4d2607f7254d5ab4a37feaa049a17c077bb50092bda8f327d2240d099716d'}, " \
						"'dob': {'date': '1990-12-20T06:00:26.436Z', 'age': 30}, " \
						"'registered': {'date': '2004-04-26T19:37:29.021Z', 'age': 16}, " \
						"'phone': '08-691-135', 'cell': '045-288-48-87', " \
						"'id': {'name': 'HETU', 'value': 'NaNNA945undefined'}, " \
						"'picture': {'large': 'https://randomuser.me/api/portraits/men/37.jpg', " \
						"'medium': 'https://randomuser.me/api/portraits/med/men/37.jpg', " \
						"'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/37.jpg'}, " \
						"'nat': 'FI'},"

		self.assertIn("gender", str(data))
		self.assertIn(random_person, str(data))
		self.assertIn('persons.json', str(file))
		self.assertIsInstance(DB, Database)
		self.assertEqual(len(data['results']), 1000)
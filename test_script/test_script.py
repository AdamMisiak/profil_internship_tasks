import unittest
import json
from script import *


# from script import calculate_how_many_days_to_birthday

class TestDataBase(unittest.TestCase):
	with open('persons.json') as file:
		data = json.load(file)
	global DB
	DB = Database(data)
	def test_database(self):

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

		self.assertIn("gender", str(self.data))
		self.assertIn(random_person, str(self.data))
		self.assertIn('persons.json', str(self.file))
		self.assertIsInstance(DB, Database)
		self.assertEqual(len(self.data['results']), 1000)


class TestFunctions(unittest.TestCase):
	def test_calculate_how_many_days_to_birthday(self):
		days_to_birthday = DB.calculate_how_many_days_to_birthday('1970-04-08')
		self.assertNotEqual(days_to_birthday, 42)
		self.assertEqual(days_to_birthday, 247)

	def test_calculate_male_female_percentage(self):
		result = DB.calculate_male_female_percentage()
		self.assertEqual(result, 'In database, there are 50.144% women and 49.856% men')

	def test_calculate_average_age(self):
		female = DB.calculate_average_age('female')
		male = DB.calculate_average_age('male')
		all = DB.calculate_average_age('all')
		error = DB.calculate_average_age('mezczyzni')
		self.assertIn('49.36', female)
		self.assertIn('48.69', male)
		self.assertIn('49.03', all)
		self.assertEqual(error, 'Wrong argument! Please type: male, female or all')

	def test_find_most_common_elements(self):
		city_result = DB.find_most_common_elements('city', '10')
		password_result = DB.find_most_common_elements('password', '10')
		error_result = DB.find_most_common_elements('password', 'ten')
		self.assertIn("'Toulon', 5", str(city_result))
		self.assertIn("'r2d2', 2", str(password_result))
		self.assertIn("ten is not a number! Input needs to be int type.", error_result)
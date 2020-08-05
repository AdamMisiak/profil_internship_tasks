import unittest
import requests
from script import *


class TestDataBase(unittest.TestCase):
	global lines
	global DB
	with open('seeds.txt') as file:
		lines = file.readlines()
	DB = Database('seeds.txt')

	def test_database(self):
		random_person = requests.get('https://randomuser.me/api/?seed=e5a40d7d4430daa1').json()

		self.assertIn("gender", str(random_person))
		self.assertIn('e5a40d7d4430daa1', str(random_person))
		self.assertIn('Database created from seeds.txt seeds file, has 1000 records', str(DB))
		self.assertIn('seeds.txt', str(self.file))
		self.assertIsInstance(DB, Database)
		self.assertEqual(len(lines), 1000)


class TestFunctions(unittest.TestCase):
	def test_calculate_how_many_days_to_birthday(self):
		days_to_birthday = DB.calculate_how_many_days_to_birthday('1970-04-08')
		self.assertNotEqual(days_to_birthday, 42)
		# CHECK YOUR DATE AT: https://www.kalendarzswiat.pl/kalkulator_urodzinowy
		self.assertEqual(days_to_birthday, 246)

	def test_calculate_male_female_percentage(self):
		result = DB.calculate_male_female_percentage()
		self.assertEqual(result, 'In database, there are 50.8% women and 49.2% men')

	def test_calculate_average_age(self):
		female = DB.calculate_average_age('female')
		male = DB.calculate_average_age('male')
		all = DB.calculate_average_age('all')
		error = DB.calculate_average_age('mezczyzni')
		self.assertIn('47.33', female)
		self.assertIn('48.39', male)
		self.assertIn('47.85', all)
		self.assertEqual(error, 'Wrong argument! Please type: male, female or all')

	def test_find_most_common_elements(self):
		city_result = DB.find_most_common_elements('city', '10')
		password_result = DB.find_most_common_elements('password', '10')
		error_result = DB.find_most_common_elements('password', 'ten')
		self.assertIn("'Dunedin', 5", str(city_result))
		self.assertIn("'wifes', 3", str(password_result))
		self.assertIn("ten is not a number! Input needs to be int type.", error_result)

	def test_find_birthdays_between_dates(self):
		dates = DB.find_birthdays_between_dates('1950/05/05', '1970/06/06')
		self.assertIn("'Emil Nielsen': datetime.date(1954, 11, 3)", str(dates))

	def test_calculate_safety_points_of_password(self):
		password_safety_one = DB.calculate_safety_points_of_password('easypassword')
		password_safety_two = DB.calculate_safety_points_of_password('Mediumpa55')
		password_safety_three = DB.calculate_safety_points_of_password('H@rdP@55w0RD')

		self.assertIn("('easypassword', 6)", str(password_safety_one))
		self.assertIn("('Mediumpa55', 9)", str(password_safety_two))
		self.assertIn("('H@rdP@55w0RD', 12)", str(password_safety_three))

	def test_check_people_passwords(self):
		safety_result = DB.check_people_passwords()
		self.assertIn("('close-up', 9)", str(safety_result))
		self.assertNotIn("('latwehaselko', 69)", str(safety_result))
		self.assertIn("('bigboobs', 6)", str(safety_result))
		# ONLY UNIQUE PASSWORDS
		self.assertEqual(len(safety_result), 937)


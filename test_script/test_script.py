import unittest
import requests
from script import *


class TestDataBase(unittest.TestCase):
	global DB
	seed = 'ec14fa7f0b8242e0'
	DB = Database(seed, 1000)
	#DB.create_database()

	def test_database(self):
		random_person = requests.get('https://randomuser.me/api/?results=1000&seed=ec14fa7f0b8242e0').json()

		self.assertIn("gender", str(random_person))
		self.assertIn('ec14fa7f0b8242e0', str(random_person))
		self.assertIn('Database created from ec14fa7f0b8242e0 seed, has 1000 records', str(DB))
		self.assertIsInstance(DB, Database)


class TestFunctions(unittest.TestCase):
	def test_calculate_how_many_days_to_birthday(self):
		days_to_birthday = DB.calculate_how_many_days_to_birthday('1970-04-08')
		self.assertNotEqual(days_to_birthday, 42)

	def test_calculate_male_female_percentage(self):
		result = DB.calculate_male_female_percentage()
		self.assertEqual(result, 'In database, there are 50.4% women and 49.6% men')

	def test_calculate_average_age(self):
		female = DB.calculate_average_age('female')
		male = DB.calculate_average_age('male')
		all = DB.calculate_average_age('all')
		error = DB.calculate_average_age('mezczyzni')
		self.assertIn('47.94', female)
		self.assertIn('48.85', male)
		self.assertIn('48.39', all)
		self.assertEqual(error, 'Wrong argument! Please type: male, female or all')

	def test_find_most_common_elements(self):
		city_result = DB.find_most_common_elements('city', '10')
		password_result = DB.find_most_common_elements('password', '10')
		error_result = DB.find_most_common_elements('password', 'ten')
		too_long_result = DB.find_most_common_elements('password', '5555')
		self.assertIn("'Hamilton', 7", str(city_result))
		self.assertIn("'milton', 2", str(password_result))
		self.assertIn("ten is not a number! Input needs to be int type.", error_result)
		self.assertIn("5555 is too big! In database there are only 1000 people.", too_long_result)

	def test_find_birthdays_between_dates(self):
		dates = DB.find_birthdays_between_dates('1950/05/05', '1970/06/06')
		wrong_dates = DB.find_birthdays_between_dates('1970/05/05', '1950/05/05')
		no_numbers_dates = DB.find_birthdays_between_dates('1970/05/05g', '1950/05/05q')
		self.assertIn("'Harley Wang': datetime.date(1961, 2, 5)", str(dates))
		self.assertIn("First date needs to be earlier then second one!", wrong_dates)
		self.assertIn("Date format needs to be YYYY/mm/dd (for example 2137/05/04)!", no_numbers_dates)

	def test_calculate_safety_points_of_password(self):
		password_safety_one = DB.calculate_safety_points_of_password('easypassword')
		password_safety_two = DB.calculate_safety_points_of_password('Mediumpa55')
		password_safety_three = DB.calculate_safety_points_of_password('H@rdP@55w0RD')

		self.assertIn("('easypassword', 6)", str(password_safety_one))
		self.assertIn("('Mediumpa55', 9)", str(password_safety_two))
		self.assertIn("('H@rdP@55w0RD', 12)", str(password_safety_three))

	def test_check_people_passwords(self):
		safety_result = DB.check_people_passwords()
		self.assertIn("('madison1', 7)", str(safety_result))
		self.assertNotIn("('latwehaselko', 69)", str(safety_result))
		self.assertIn("('penetration', 6)", str(safety_result))
		# ONLY UNIQUE PASSWORDS
		self.assertEqual(len(safety_result), 934)


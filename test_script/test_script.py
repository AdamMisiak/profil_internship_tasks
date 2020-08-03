import pytest
import unittest
import json
from script import Database

class TestStringMethods(unittest.TestCase):

	def test_creating_instance(self):
		with open('persons.json') as file:
			data = json.load(file)
		DB = Database(data)
		DB.create_database()

		self.assertEqual('Database persons.json created from persons.json file, has 1000 records', print(DB))

	#assert '1000 records' in DB
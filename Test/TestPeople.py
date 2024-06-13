import unittest
import sys
import os

from Utils.People import People

# Ajoutez le répertoire du module Utils au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Utils')))


class TestPeople(unittest.TestCase):
    def test_getName(self):
        person = People("Laura")
        self.assertEqual(person.getName, "Laura")

    def test_setName(self):
        person = People("Laura")
        self.assertEqual(person.getName, "Laura")
        person.setName("KIKI")
        self.assertEqual(person.getName, "KIKI")


if __name__ == '__main__':
    unittest.main()

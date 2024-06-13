import unittest
import sys
import os

from Utils import People

class TestPeople(unittest.TestCase):
    def test_getName(self):
        person = People("Laura")
        self.assertEqual(person.getName, "Laura")

if __name__ == '__main__':
    unittest.main()

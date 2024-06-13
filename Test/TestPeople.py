import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Utils')))

from people import People

class TestPeople(unittest.TestCase):
    def test_getName(self):
        person = People("Laura")
        self.assertEqual(person.getName, "Laura")

if __name__ == '__main__':
    unittest.main()

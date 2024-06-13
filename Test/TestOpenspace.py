import os
import sys
import unittest
from typing import List

from Utils.Openspace import Openspace
from Utils.People import People
from Utils.Table import Table


class TestOpenspace(unittest.TestCase):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Utils')))

    def setUp(self):
        self.openspace = Openspace(24)
        self.openspace5 = Openspace(5)

    def testGetNbCapacity(self):
        """Test the get nb capacity function."""
        self.assertEqual(self.openspace.getNbCapacity, 24)
        self.assertNotEqual(self.openspace5.getNbCapacity, 24)

    def organised(self, listName: List[List[People | str]]) -> None:
        """Test the get nb capacity function."""

    def addOpenspace(self, table: Table) -> None:
        """Test if the table is added to the open space."""

    def store(self, filename: str) -> None:
        """Test if stores the organization of the openspace into an Excel file."""

import unittest

from Utils.Table import Table


class TestTable(unittest.TestCase):
    """ Class that will test all Table functions """

    def testHasFreeSpot(self):
        """Test the HasFreeSpot function."""
        table = Table(4)
        self.assertTrue(table.hasFreeSpot())

        table.assignSeat("Alice")
        self.assertTrue(table.hasFreeSpot())  # Should still have free spots after assigning one seat

        table.assignSeat("Bob")
        table.assignSeat("Charlie")
        table.assignSeat("Dave")
        self.assertFalse(table.hasFreeSpot())  # Should have 4 people seated and no more space

    def testAssignSeat(self):
        """Test the Assign Seat function."""
        table = Table(4)
        self.assertTrue(table.assignSeat("Test"))
        self.assertTrue(table.assignSeat("Truc"))
        self.assertTrue(table.assignSeat("Machin"))
        self.assertTrue(table.assignSeat("Bidule"))
        self.assertFalse(table.assignSeat("Poney")) # No more free place

    def testGetLeftCapacity(self):
        """Test the Get left capacity function."""
        table = Table(4)
        self.assertEqual(table.getLeftCapacity(), 4)

        self.assertTrue(table.assignSeat("Test"))
        self.assertEqual(table.getLeftCapacity(), 3)

        self.assertTrue(table.assignSeat("Truc"))
        self.assertEqual(table.getLeftCapacity(), 2)

        self.assertTrue(table.assignSeat("Machin"))
        self.assertEqual(table.getLeftCapacity(), 1)

        self.assertTrue(table.assignSeat("Bidule"))
        self.assertEqual(table.getLeftCapacity(), 0)

        self.assertNotEqual(table.getLeftCapacity(), 4)


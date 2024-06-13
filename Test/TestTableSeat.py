import unittest

from Utils.Table import Table, Seat


class TestTable(unittest.TestCase):
    """Class that will test all Table functions"""

    def setUp(self):
        self.table = Table(4)

    def testHasFreeSpot(self):
        """Test the hasFreeSpot function."""
        self.assertTrue(self.table.hasFreeSpot())

        self.table.assignSeat("Alice")
        self.assertTrue(
            self.table.hasFreeSpot()
        )  # Should still have free spots after assigning one seat

        self.table.assignSeat("Bob")
        self.table.assignSeat("Charlie")
        self.table.assignSeat("Dave")
        self.assertFalse(
            self.table.hasFreeSpot()
        )  # Should have 4 people seated and no more space

    def testAssignSeat(self):
        """Test the assignSeat function."""
        self.assertTrue(self.table.assignSeat("Test"))
        self.assertTrue(self.table.assignSeat("Truc"))
        self.assertTrue(self.table.assignSeat("Machin"))
        self.assertTrue(self.table.assignSeat("Bidule"))
        self.assertFalse(self.table.assignSeat("Poney"))  # No more free place

    def testGetLeftCapacity(self):
        """Test the getLeftCapacity property."""
        self.assertEqual(self.table.getLeftCapacity, 4)  # Initial capacity should be 4

        self.assertTrue(self.table.assignSeat("Test"))
        self.assertEqual(self.table.getLeftCapacity, 3)

        self.assertTrue(self.table.assignSeat("Truc"))
        self.assertEqual(self.table.getLeftCapacity, 2)

        self.assertTrue(self.table.assignSeat("Machin"))
        self.assertEqual(self.table.getLeftCapacity, 1)

        self.assertTrue(self.table.assignSeat("Bidule"))
        self.assertEqual(self.table.getLeftCapacity, 0)


class TestSeat(unittest.TestCase):
    """Class that will test all Seat functions"""

    def setUp(self):
        self.seat = Seat()  # Initialize a Seat object for each test

    def test_initial_state(self):
        self.assertTrue(self.seat.free)
        self.assertEqual(self.seat.occupant, "")

    def test_setOccupant_success(self):
        self.assertTrue(self.seat.setOccupant("Alice"))
        self.assertFalse(self.seat.free)
        self.assertEqual(self.seat.occupant, "Alice")

    def test_setOccupant_failure(self):
        self.assertTrue(self.seat.setOccupant("Bob"))
        self.assertFalse(self.seat.setOccupant("Charlie"))
        self.assertEqual(self.seat.occupant, "Bob")

    def test_removeOccupant(self):
        self.seat.setOccupant("Eve")
        self.assertFalse(self.seat.free)
        self.assertEqual(self.seat.removeOccupant(), "Eve")
        self.assertTrue(self.seat.free)
        self.assertEqual(self.seat.occupant, "")

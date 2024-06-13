import random
from typing import List

import pandas as pd

from People import People
from Table import Table


class Openspace:
    def __init__(self, nbCapacity: int = 24):
        """
        Initializes an Openspace with a specified capacity.

        Args:
            nbCapacity (int): The maximum capacity of the openspace. Default is 24.
        """
        self.nbCapacity = nbCapacity
        self.openspace = []

    @property
    def getNbCapacity(self) -> int:
        """
        Returns the maximum capacity of the openspace.

        Returns:
            int: Maximum capacity of the openspace.
        """
        return self.nbCapacity

    def organised(self, listName: List[People | str]) -> None:
        """
        Organizes people into tables in the openspace.

        Args:
            listName (List[People | str]): List of people names or empty strings for empty seats.
        """
        table = Table()
        countBlank = 0

        # Shuffle the list of names
        random.shuffle(listName)

        # Add all people to a table
        for i in listName:
            # Check if the table is full
            if table.getLeftCapacity() - countBlank <= 0:
                self.addOpenspace(table)
                table = Table()

                countBlank = 0

            if i != '':
                self.openspace.assignSeat(i)
            else:
                countBlank += 1

    def addOpenspace(self, table: Table) -> None:
        """
        Adds a table to the openspace.

        Args:
            table (Table): The table to add to the openspace.
        """

        self.openspace.append(table)

    def store(self, filename: str) -> None:
        """
        Stores the organization of the openspace into an Excel file.

        Args:
            filename (str): The name of the Excel file where the data will be stored.
        """
        data = []
        for table in self.openspace:
            table_data = [person.getName() if isinstance(person, People) else '' for person in table]
            print(table_data)
            data.append(table_data)

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Write to an Excel file
        df.to_excel(filename, index=False, header=False)


import random
from typing import List, Union
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
    
    def organised(self, listName: List[Union[People, str]]) -> None:
        """
        Organizes people into tables in the openspace.

        Args:
            listName (List[Union[People, str]]): List of people names or empty strings for empty seats.
        """
        listTable = []
        countBlank = 0

        # Shuffle the list of names
        random.shuffle(listName)
        
        # Add all people to a table
        for i in listName:
            # Check if the table is full
            if len(listTable) >= Table.getCapacity() - countBlank:
                self.addOpenspace(listTable)
                listTable = []
                countBlank = 0

            if i != '':
                listTable.append(i)
            else:
                countBlank += 1

        # Add the last table if it's not empty
        if listTable:
            self.addOpenspace(listTable)

    def addOpenspace(self, listTable: List[Union[People, str]]) -> None:
        """
        Adds a table to the openspace.

        Args:
            listTable (List[Union[People, str]]): List of people or empty seats to add to a table.
        """
        self.openspace.append(listTable)

    def store(self, filename: str) -> None:
        """
        Stores the organization of the openspace into an Excel file.

        Args:
            filename (str): The name of the Excel file where the data will be stored.
        """
        data = []
        for table in self.openspace:
            table_data = [person.getName() if isinstance(person, People) else '' for person in table]
            data.append(table_data)

        df = pd.DataFrame(data)

        df.to_excel(filename, index=False, header=False)
        

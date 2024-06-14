import random
from typing import List
import pandas as pd

from Utils.People import People
from Utils.Table import Table
from Utils.Config import Config


class Openspace:
    def __init__(self, config):
        """
        Initializes an Openspace with a specified capacity.

        Args:
            nbCapacity (int): The maximum capacity of the openspace. Default is 24.
        """
        self.nbCapacity = config.getConfig['nbCapacity']
        self.openspace = []
        self.config = config
        

    @property
    def getNbCapacity(self) -> int:
        """
        Returns the maximum capacity of the openspace.

        Returns:
            int: Maximum capacity of the openspace.
        """
        return self.nbCapacity
    
    def setNbCapacity(self, nbMax:int) -> None:
        """
            Change the number of nbCapacity.
        """
        self.nbCapacity = nbMax

    def organised(self, listName: List[List[People | str]]) -> None:
        """
        Organizes people into tables in the openspace.

        Args:
            listName (List[List[People|str]]): List of people names or empty strings for empty seats.
        """
        table = Table(self.config)
        countBlank = 0

        # Shuffle the list of names
        
        random.shuffle(listName)

        # Add all people to a table
        print(len(listName))

        for i in listName:
            # Check if the table is full
            if table.getLeftCapacity - countBlank <= 0 and len(self.openspace) != self.config.getConfig['limitTable']:
                self.addOpenspace(table)
                table = Table(self.config)
                countBlank = 0

            if i != "":
                table.assignSeat(i)
            else:
                countBlank += 1
                
        # Add the last table if it's not empty
        if table:
            self.addOpenspace(table)

        table = Table(self.config)
        [self.openspace.append(table) for _ in range(self.config.getConfig['limitTable']) if len(self.openspace) != self.config.getConfig['limitTable']]

        remaining_people = listName[self.config.getConfig['limitTable']*self.config.getConfig['capacity'] :]
        if remaining_people:
            print(
                "==============\n"
                "These people could not be seated due to capacity limits:",
            )
            for i in (remaining_people):
                print(i.getName)
           
            print("==============")

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
            table_data = [seat.getOccupant.getName if seat.getOccupant != "" else "" for seat in table.getSeats]
            data.append(table_data)
    
    
        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Write to an Excel file
        df.to_excel(filename, index=False, header=False)

    def display(self) -> None:
        for index, table in enumerate(self.openspace, start=1):
            print(f"Table {index}")
            for index, seat in enumerate(table.seats, start=1):
                print(f"  Seat {index}: {seat.__str__()}")


from typing import List

import pandas as pd
import json
from Utils.People import People
from Utils.Openspace import Openspace
from copy import deepcopy

from Utils.Table import Table


# Factory class to manage people
class Factory:
    def __init__(self):
        """
        Initialize a Factory object with an empty list to store Person objects.
        """
        self._peopleList = []

    @property
    def getPeopleList(self):
        """
        Property to return a deep copy of the list of Person objects.

        Returns:
        - list: A deep copy of the list containing Person objects.
        """
        return deepcopy(self._peopleList)

    def addPerson(self, person: People):
        """
        Add a Person object to the factory's list of people.

        Args:
        - person (Person): A Person object to be added to the list.

        Raises:
        - ValueError: If the input is not an instance of Person.
        """
        if isinstance(person, People):
            self._peopleList.append(person)
        else:
            raise ValueError("Only instances of Person can be added to the list")

    def loadConfigFromJson(self, config_file: str) -> Openspace:
        try:
            with open(config_file, 'r') as f:
                config_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{config_file}' not found")

        openspace_capacity = config_data.get('openspace_capacity', 24)
        tables_config = config_data.get('tables', [])

        openspace = Openspace(nbCapacity=openspace_capacity)

        # Calculate the total capacity needed to fill the openspace
        total_capacity_needed = openspace_capacity
        current_capacity = 0

        # Continue adding tables until the total capacity meets or exceeds the required openspace capacity
        while current_capacity < total_capacity_needed:
            # Iterate through each table configuration in the tables configuration list
            for table_config in tables_config:
                # Exit the loop if the current capacity meets or exceeds the required openspace capacity
                if current_capacity >= total_capacity_needed:
                    break

                # Get the capacity of the current table from the table configuration; default to 4 if not specified
                capacity = table_config.get('capacity', 4)

                # Calculate remaining capacity needed to reach the openspace capacity
                remaining_capacity = total_capacity_needed - current_capacity

                # Check if the capacity of the current table does not exceed the remaining capacity needed
                if capacity <= remaining_capacity:
                    table = Table(capacity=capacity)
                    openspace.addOpenspace(table)
                    current_capacity += capacity
        return openspace


    def loadPeopleFromExcel(self, file_path: str, openspace: Openspace):
        """
        Load people from an Excel file into the factory.

        Args:
        - file_path (str): Path to the Excel file containing names under 'Colleagues' column.

        Raises:
        - ValueError: If the 'Colleagues' column is not found in the Excel file.
        - FileNotFoundError: If the specified file_path does not exist.
        """
        try:
            df = pd.read_excel(file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found")
        
        if 'Colleagues' in df.columns:
            for _, row in df.iterrows():
                person = People(name=row['Colleagues'])
                self.addPerson(person)
        else:
            raise ValueError("Column 'Colleagues' not found in the Excel file")

        while openspace.getNbCapacity > len(self._peopleList):
            self._peopleList.append('')


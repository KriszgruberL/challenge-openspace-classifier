import random
from typing import List, Union
import pandas as pd
from People import People  # Assurez-vous que le module People existe et contient la classe People
from Table import Table  # Assurez-vous que le module Table existe et contient la classe Table

class Openspace:
    def __init__(self, nbCapacity: int = 24):
        """
        Initialise un Openspace avec une capacité spécifiée.

        Args:
            nbCapacity (int): La capacité maximale de l'openspace. Par défaut, 24.
        """
        self.nbCapacity = nbCapacity
        self.openspace = []

    @property
    def getNbCapacity(self) -> int:
        """
        Renvoie la capacité maximale de l'openspace.

        Returns:
            int: Capacité maximale de l'openspace.
        """
        return self.nbCapacity
    
    def organised(self, listName: List[Union[People, str]]) -> None:
        """
        Organise les personnes dans des tables dans l'openspace.

        Args:
            listName (List[Union[People, str]]): Liste des noms des personnes ou des chaînes vides pour les places vides.
        """
        listTable = []
        countBlank = 0

        # Mélange la liste de noms
        random.shuffle(listName)
        
        # Ajoute toutes les personnes à une table
        for i in listName:
            # Vérifie si la table est pleine
            if len(listTable) >= Table.getCapacity() - countBlank:
                self.addOpenspace(listTable)
                listTable = []
                countBlank = 0

            if i != '':
                listTable.append(i)
            else:
                countBlank += 1

        # Ajoute la dernière table si elle n'est pas vide
        if listTable:
            self.addOpenspace(listTable)

    def addOpenspace(self, listTable: List[Union[People, str]]) -> None:
        """
        Ajoute une table à l'openspace.

        Args:
            listTable (List[Union[People, str]]): Liste des personnes ou des places vides à ajouter à une table.
        """
        self.openspace.append(listTable)

    def store(self, filename: str) -> None:
        """
        Stocke l'organisation de l'openspace dans un fichier Excel.

        Args:
            filename (str): Le nom du fichier Excel où les données seront stockées.
        """
        data = []
        for table in self.openspace:
            table_data = [person.getName() if isinstance(person, People) else '' for person in table]
            data.append(table_data)

        # Convertir en DataFrame
        df = pd.DataFrame(data)

        # Écrire dans un fichier Excel
        df.to_excel(filename, index=False, header=False)

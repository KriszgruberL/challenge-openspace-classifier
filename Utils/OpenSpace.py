import People
import List
import Table
import random
import pandas as pd

class Openspace:
    def __init__(self, nbCapacity:int=24):
        self.nbCapacity = nbCapacity
        self.openspace = []

    @property
    def getNbCapacity(self) -> None:
        return self.nbCapacity
    
    def organised(self, listName: List[People|'']) -> None:
        listTable = []
        countBlank = 0

        # shuffle the list of all name
        random.shuffle(listName)
        
        # add all people on a table
        for i in listName:
            #if i.getWantPlace
                # check in list if alreayd added and table is not full

            if len(listTable) >= Table.getCapacity() - countBlank:
                self.addOpenspace(listTable)
                listTable = []
                countBlank = 0

            if i != '':
                listTable.append(i)
            else:
                countBlank += 1

    def addOpenspace(self, listTable: List[List[People]]) -> None:
        self.openspace.append(listTable)

    def store(self, filename:str) -> None:
        data = []
        for table in self.openspace:
            table_data = [person.getName for person in table]
            data.append(table_data)

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Write to Excel file
        df.to_excel(filename, index=False, header=False)
    

            
            
        

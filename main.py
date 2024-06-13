from Utils.Factory import Factory
from Utils.Openspace import Openspace

def main():
    facto = Factory()
    facto.loadPeopleFromExcel("./Data/Example_Excel_Template.xlsx")

    openspace = Openspace()
    openspace.organised(facto.getPeopleList)
    openspace.store("./Data/ordered.xlsx")
    
    print("dont !")
    return 0

if __name__ == "__main__":
    main()

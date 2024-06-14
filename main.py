from Utils.Factory import Factory
from Utils.Openspace import Openspace


def main():
    facto = Factory()
    openspace = Openspace()
    
    facto.loadPeopleFromExcel("./Data/Example_Excel_Template.xlsx", openspace)
    openspace.organised(facto.getPeopleList)
    openspace.store("./Data/ordered.xlsx")
    openspace.display()

    print("done !")
    return 0


if __name__ == "__main__":
    main()

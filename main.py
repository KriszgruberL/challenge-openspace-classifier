from Utils.Factory import Factory
from Utils.Openspace import Openspace
from Utils.Config import Config


def main():
    config = Config()
    config.loadOrCreateConfig() 

    openspace = Openspace(config)
    facto = Factory()
      
    facto.loadPeopleFromExcel("./Data/Example_Excel_Template.xlsx", openspace)
    openspace.organised(facto.getPeopleList)
    openspace.store("./Data/ordered.xlsx")

    openspace.display()

    print("done !")
    return 0


if __name__ == "__main__":
    main()

from Utils import Factory
from Utils import Openspace


def main():
    facto = Factory()
    facto.loadPeopleFromExcel("./Data/")

    openspace = Openspace()
    openspace.organised(facto.getPeopleList)
    openspace.store("./Data/ordered.xlsx")

    print("dont !")
    return 0


if __name__ == "__main__":
    main()

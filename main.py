from Utils.Factory import Factory
from Utils.Openspace import Openspace
import os
import platform


def main():
    if platform.system() == 'Windows' :
        os.system('cls')
    else :
        os.system("clear")


    seats = 15
    people = 30
    freeSeats = 2

    print("""
+-------------------+
|       Hello!      |
+-------------------+""")

    choice = '0'

    while choice != '9':
        choice = input("""
1. Shuffle people around
2. How much seats are in the room ?
3. How many people in the room ? 
4. How many seats are empty ? 
9. Exit
Enter your choice : """)

        match choice:
            case '1':
                print("Shuffling people around...\n")
                facto = Factory()
                openspace = Openspace()

                facto.loadPeopleFromExcel("./Data/Example_Excel_Template.xlsx", openspace)
                openspace.organised(facto.getPeopleList)
                openspace.store("./Data/ordered.xlsx")
                openspace.display()
                break
            case '2':
                print(f"There is {seats} seats in this openspace")
                break
            case '3':
                print(f"There is {people} people in this openspace")
                break
            case '4':
                print(f"There is {freeSeats} free seats in this openspace")
                break
            case '9':
                print("Okay bye")
                break
            case _:
                print("Invalid choice, please try again.")

        print("done !")
        return 0

if __name__ == "__main__":
    main()

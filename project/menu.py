from project.plant_list import add_new_plant
from project.plant_list import print_list


def choice (list_of_plants):
    while True:
        answer = input("Would you like to add a new plant? (Y/N): ")
        if answer == "Y":
            add_new_plant(list_of_plants)
            print_list(list_of_plants)
        elif answer == "N":
            print("Thank you for using Plantopedia")
            break
        else:
            print("Wrong input")
            continue

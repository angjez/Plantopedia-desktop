from project.plant_list import list_of_plants
from project.plant_list import add_new_plant
import time
import sys

if not list_of_plants:
    print("You have no plants saved")
    time.sleep(2)
    answer = input("Would you like to add a new plant? (Y/N): ")
    if answer == "Y":
        add_new_plant()
    elif answer == "N":
        print("Thank you for using Plantopedia")
        sys.exit(0)
    else:
        print("Wrong input")
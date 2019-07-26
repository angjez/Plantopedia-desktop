from project.menu import choice
from project.plant_list import print_list
from project.pickle_data import load_data
from project.plant_def import Plants
import time
import sys


def main():
    list_of_plants = []
    load_data(list_of_plants)

    if not list_of_plants:
        print("You have no plants saved")
        time.sleep(1)
        choice(list_of_plants)

    if list_of_plants:
        print_list(list_of_plants)
        choice(list_of_plants)


main()

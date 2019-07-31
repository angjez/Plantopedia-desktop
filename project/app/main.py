#!/usr/bin/env python


def main():
    from project.app.menu import choice
    from project.app.pickle_data import load_data
    from project.app.pickle_data import store_data
    from project.app.pickle_data import clear_file
    from project.app.plant_list import ListOfPlants

    list_of_plants = ListOfPlants()
    load_data(list_of_plants)

    choice(list_of_plants)

    clear_file()
    store_data(list_of_plants.list)


main()

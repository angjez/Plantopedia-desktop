#!/usr/bin/env python


def main():
    from project.menu import choice
    from project.pickle_data import load_data
    from project.pickle_data import store_data
    from project.pickle_data import clear_file
    from project.plant_list import ListOfPlants
    from project.kivy_interface.interface_main import Main

    list_of_plants = ListOfPlants()
    load_data(list_of_plants)

    choice(list_of_plants)

    clear_file()
    store_data(list_of_plants.list)


main()

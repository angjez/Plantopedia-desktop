#!/usr/bin/env python


def main():
    from project.menu import choice
    from project.plant_list import ListOfPlants
    from project.pickle_data import load_data
    from project.pickle_data import store_data
    from project.pickle_data import clear_file

    load_data()

    choice()

    clear_file()
    store_data()


main()

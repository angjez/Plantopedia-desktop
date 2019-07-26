def main():
    from project.menu import choice
    from project.pickle_data import load_data
    from project.plant_list import store_data
    from project.pickle_data import clear_file

    list_of_plants = []
    load_data(list_of_plants)

    choice(list_of_plants)

    clear_file()
    store_data(list_of_plants)


main()

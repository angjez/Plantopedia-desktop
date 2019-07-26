from project.plant_def import Plants
from project.pickle_data import store_data


def add_new_plant(list_of_plants):
    new_plant = Plants(input("Common name: "), input("Botanical name: "), input("Sun exposure: "), input("Water: "), input("Soil: "), input("Repotting: "), input("Size: "))
    list_of_plants.append(new_plant)
    store_data(new_plant)


def print_variables(plant):
    print("Common name: " + str(plant.common_name))
    print("Botanical name: " + str(plant.botanical_name))
    print("Sun exposure: " + str(plant.sun_exposure))
    print("Water: " + str(plant.water))
    print("Soil: " + str(plant.soil))
    print("Repotting: " + str(plant.repotting))
    print("Size: " + str(plant.size))


def print_list(list_of_plants):
    for plant in range(len(list_of_plants)):
        print_variables(list_of_plants[plant])
        print("")
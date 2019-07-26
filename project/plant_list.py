from project.plant_def import Plants


def add_new_plant(list_of_plants):
    new_plant = Plants(input("Common name: "), input("Botanical name: "), input("Sun exposure: "), input("Water: "), input("Soil: "), input("Repotting: "), input("Size: "))
    list_of_plants.append(new_plant)


def print_variables(plant):
    print("Common name: " + str(plant.common_name))
    print("Botanical name: " + str(plant.botanical_name))
    print("Sun exposure: " + str(plant.sun_exposure))
    print("Water: " + str(plant.water))
    print("Soil: " + str(plant.soil))
    print("Repotting: " + str(plant.repotting))
    print("Size: " + str(plant.size))


def print_list(list_of_plants):
    if list_of_plants:
        print("Your plants: ")
        print("")
        for plant in range(len(list_of_plants)):
            print_variables(list_of_plants[plant])
            print("")
    else:
        print("You have no saved plants.")


def delete_from_list (list_of_plants, to_delete):
    for plant in list_of_plants:
        if plant.common_name == to_delete:
            list_of_plants.remove(plant)
            return True
    return False



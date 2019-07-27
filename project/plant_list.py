from project.plant_def import Plant


class ListOfPlants:
    list_of_plants = []

    @staticmethod
    def add_new_plant(list_of_plants):
        new_plant = Plant(input("Common name: "), input("Botanical name: "), input("Sun exposure: "), input("Water: "), input("Soil: "), input("Repotting: "), input("Size: "))
        list_of_plants.append(new_plant)

    @staticmethod
    def print_list(list_of_plants):
        if list_of_plants:
            print("Your plants: ")
            print("")
            for plant in range(len(list_of_plants)):
                list_of_plants[plant].print_variables()
                print("")
        else:
            print("You have no saved plants.")

    @staticmethod
    def delete_from_list (list_of_plants, to_delete):
        for plant in list_of_plants:
            if plant.common_name == to_delete:
                list_of_plants.remove(plant)
                return True
        return False



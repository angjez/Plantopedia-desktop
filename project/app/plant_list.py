from project.app.plant_def import Plant


class ListOfPlants:
    def __init__(self):
        self.list = []

    def add_new_plant(self):
        new_plant = Plant(input("Common name: "), input("Botanical name: "), input("Sun exposure: "), input("Water: "), input("Soil: "), input("Repotting: "), input("Size: "))
        self.list.append(new_plant)

    def add_defined_plant(self, defined_plant):
        self.list.append(defined_plant)

    def print_list(self):
        if self.list:
            print("Your plants: ")
            print("")
            for plant in range(len(self.list)):
                self.list[plant].print_variables()
                print("")
        else:
            print("You have no saved plants.")

    def delete_from_list(self, to_delete, obj):
        for plant in self.list:
            if plant.common_name == to_delete:
                self.list.remove(plant)



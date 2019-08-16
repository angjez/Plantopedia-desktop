from project.app.plant_def import Plant


class ListOfPlants:
    def __init__(self):
        self.list = []

    def add_defined_plant(self, defined_plant):
        self.list.append(defined_plant)

    def delete_from_list(self, to_delete):
        for plant in range(len(self.list)):
            if self.list[plant].common_name == to_delete:
                self.list.remove(self.list[plant])
                break



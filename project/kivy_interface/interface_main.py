import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


# screens


class Manager(ScreenManager):
    def __init__(self, list_of_plants, **kwargs):
        super(Manager, self).__init__(**kwargs)
        from project.kivy_interface.layouts import MainBoxes
        self.list = []
        self.screen = []
        self.menu_screen = Screen(name="Menu")
        self.menu_screen.add_widget(MainBoxes(list_of_plants, self))
        self.add_widget(self.menu_screen)
        self.current = "Menu"

    def push_plant_screens(self, list_of_plants, plant_boxes):
        for n in range(len(list_of_plants.list)):
            from project.kivy_interface.layouts import PlantProperties
            self.list.append(PlantProperties(list_of_plants.list[n], self, list_of_plants, plant_boxes))
            self.screen.append(Screen(name=list_of_plants.list[n].common_name))
            self.screen[n].add_widget(self.list[n])
            self.add_widget(self.screen[n])

    def switch_screens(self, name, obj):
        self.current = name

    def goto_menu(self):
        self.current = "Menu"

    def add_screen(self, list_of_plants, plant_boxes):
        from project.kivy_interface.layouts import PlantProperties
        new_screen = Screen(name=list_of_plants.list[-1].common_name)
        new_screen.add_widget(PlantProperties(list_of_plants.list[-1], self, list_of_plants, plant_boxes))
        self.add_widget(new_screen)
        self.current = list_of_plants.list[-1].common_name

    def delete_plant(self, list_of_plants, plant_boxes, obj):
        from project.app.plant_list import ListOfPlants
        from project.kivy_interface.layouts import PlantBoxes
        from project.app.pickle_data import store_data
        from project.app.pickle_data import clear_file
        screen_to_delete = self.current
        ListOfPlants.delete_from_list(list_of_plants, screen_to_delete)
        # updating the file after changing the list of plants
        clear_file()
        store_data(list_of_plants.list)
        self.goto_menu()
        index = 0
        for n in range(len(self.screen)):
            if self.screen[n].name == screen_to_delete:
                screen_to_delete = self.screen[n]
                self.remove_widget(screen_to_delete)
                index = n
        PlantBoxes.remove_button(plant_boxes, index)

    def delete_multiple_plants(self, list_of_plants, plant_boxes, n):
        from project.app.pickle_data import store_data
        from project.app.pickle_data import clear_file
        from project.kivy_interface.layouts import PlantBoxes
        from project.app.plant_list import ListOfPlants
        ListOfPlants.delete_from_list(list_of_plants, self.screen[n].name)
        clear_file()
        store_data(list_of_plants.list)
        self.remove_widget(self.screen[n])
        PlantBoxes.remove_button(plant_boxes, n)

    def delete_multiple_screens(self, list_of_plants, plant_boxes, obj):
        self.add_widget(DeleteMultiple(list_of_plants, self, plant_boxes))
        DeleteMultiple.name = "Delete multiple"
        self.current = "Delete multiple"

    def add_plant_screen(self, list_of_plants, plant_boxes, obj):
        self.add_widget(AddPlant(self, list_of_plants, plant_boxes))
        AddPlant.name = "Add plant"
        self.current = "Add plant"


class AddPlant(Screen):
    def __init__(self, sm, list_of_plants, plant_boxes, **kwargs):
        super(AddPlant, self).__init__(**kwargs)
        from project.kivy_interface.layouts import NewPlant
        new_plant_page = NewPlant(list_of_plants, sm, plant_boxes)
        self.add_widget(new_plant_page)


class DeleteMultiple(Screen):
    def __init__(self, list_of_plants, sm, plant_boxes, **kwargs):
        super(DeleteMultiple, self).__init__(**kwargs)
        from project.kivy_interface.layouts import DeleteMultipleBoxes
        from project.kivy_interface.layouts import DeleteMultipleCheckboxes
        del_multiple_checkboxes = DeleteMultipleCheckboxes(list_of_plants)
        delete_multiple = DeleteMultipleBoxes(list_of_plants, del_multiple_checkboxes, sm, plant_boxes)
        self.add_widget(delete_multiple)


class MainApp(App):
    def build(self):
        from project.app.pickle_data import load_data
        from project.app.plant_list import ListOfPlants

        self.title = "Plantopedia"
        list_of_plants = ListOfPlants()
        load_data(list_of_plants)

        return Manager(list_of_plants)


if __name__ == '__main__':
    MainApp().run()
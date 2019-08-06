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

    def push_plant_screens(self, list_of_plants):
        for n in range(len(list_of_plants)):
            from project.kivy_interface.layouts import PlantProperties
            self.list.append(PlantProperties(list_of_plants[n], self, list_of_plants))
            self.screen.append(Screen(name=list_of_plants[n].common_name))
            self.screen[n].add_widget(self.list[n])
            self.add_widget(self.screen[n])

    def switch_screens(self, name, obj):
        self.current = name

    def goto_menu(self):
        self.current = "Menu"

    def add_plant_screen(self, list_of_plants, obj):
        self.add_widget(AddPlant(self, list_of_plants))
        AddPlant.name = "Add plant"
        self.current = "Add plant"

    def add_screen(self, list_of_plants):
        from project.kivy_interface.layouts import PlantProperties
        new_screen = Screen(name=list_of_plants[-1].common_name)
        new_screen.add_widget(PlantProperties(list_of_plants[-1], self, list_of_plants))
        self.add_widget(new_screen)
        self.current = list_of_plants[-1].common_name

    def add_button(self):
        pass


class AddPlant(Screen):
    def __init__(self, sm, list_of_plants, **kwargs):
        super(AddPlant, self).__init__(**kwargs)
        from project.kivy_interface.layouts import NewPlant
        new_plant_page = NewPlant(list_of_plants, sm)
        self.add_widget(new_plant_page)


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
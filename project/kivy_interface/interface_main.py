import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


# screens


class Manager(ScreenManager):
    def __init__(self, list_of_plants, **kwargs):
        super(Manager, self).__init__(**kwargs)
        self.list = []
        self.screen = []
        menu_screen = MenuScreen(list_of_plants, self)
        self.add_widget(menu_screen)
        MenuScreen.name = "Menu"
        self.current = "Menu"

    def push_plant_screens(self, list_of_plants):
        from project.kivy_interface.layouts import PlantProperties
        for n in range(len(list_of_plants)):
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


class MenuScreen(Screen):
    def __init__(self, list_of_plants, sm, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        from project.kivy_interface.layouts import MainBoxes
        menu_page = MainBoxes(list_of_plants, sm)
        self.add_widget(menu_page)


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
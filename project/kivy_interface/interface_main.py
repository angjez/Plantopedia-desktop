import kivy
kivy.require('1.11.0')

from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


# screens


class Manager(ScreenManager):

    def __init__(self, list_of_plants, **kwargs):
        super(Manager, self).__init__(**kwargs)
        self.list = []
        self.screen = []
        self.add_widget(MenuScreen(list_of_plants, self))
        MenuScreen.name = "Menu"
        self.current = "Menu"

    def push_plant_screens(self, list_of_plants):
        from project.kivy_interface.layouts import PlantProperties
        for n in range(len(list_of_plants)):
            self.list.append(PlantProperties(list_of_plants[n], self))
            self.screen.append(Screen(name=list_of_plants[n].common_name))
            self.screen[n].add_widget(self.list[n])
            self.add_widget(self.screen[n])

    def switch_screens(self, name, obj):
        self.current = name

    def goto_menu(self):
        self.current = "Menu"


class MenuScreen(Screen):

    def __init__(self, list_of_plants, sm, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        from project.kivy_interface.layouts import MainBoxes
        menu_page = MainBoxes(list_of_plants, sm)
        self.add_widget(menu_page)


class MainApp(App):
    def build(self):
        from project.app.pickle_data import load_data
        from project.app.pickle_data import store_data
        from project.app.pickle_data import clear_file
        from project.app.plant_list import ListOfPlants

        self.title = "Plantopedia"

        list_of_plants = ListOfPlants()
        load_data(list_of_plants)
        clear_file()
        store_data(list_of_plants.list)

        return Manager(list_of_plants)


if __name__ == '__main__':
    MainApp().run()
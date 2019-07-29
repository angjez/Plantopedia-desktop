import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class MenuBoxes(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuBoxes, self).__init__(**kwargs)
        self.orientation = "horizontal"

        add_button = Button(text="Add", size_hint=(.1, .1))

        delete_button = Button(text="Delete", size_hint=(.1, .1))

        edit_button = Button(text="Edit", size_hint=(.1, .1))

        for but in [add_button, delete_button, edit_button]:
            self.add_widget(but)

    def event_add_plant(self, obj):
        print("Typical event from", obj)

    def event_delete_plant(self, obj):
        print("Typical event from", obj)

    def event_edit_plant(self, obj):
        print("Typical event from", obj)


class PlantBoxes(BoxLayout):

    def __init__(self, list_of_plants, **kwargs):
        super(PlantBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        button = []

        for n in range(len(list_of_plants.list)):
            button.append(Button(text=list_of_plants.list[n].common_name))
            self.add_widget(button[n])

    def event_show_plant(self, obj):
        print("Typical event from", obj)


class MainBoxes(BoxLayout):

    def __init__(self, list_of_plants, **kwargs):
        super(MainBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        plant_boxes = PlantBoxes(list_of_plants)
        menu_boxes = MenuBoxes()
        self.add_widget(plant_boxes)
        self.add_widget(menu_boxes)


class MenuScreen(Screen):
    def __init__(self,list_of_plants, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        menu_page = MainBoxes(list_of_plants)
        self.add_widget(menu_page)


class MainApp(App):
    def build(self):
        from project.pickle_data import load_data
        from project.pickle_data import store_data
        from project.pickle_data import clear_file
        from project.plant_list import ListOfPlants

        self.title = "Plantopedia"

        list_of_plants = ListOfPlants()
        load_data(list_of_plants)
        sm = ScreenManager()
        sm.add_widget(MenuScreen(list_of_plants, name='Menu'))
        clear_file()
        store_data(list_of_plants.list)

        return sm


if __name__ == '__main__':
    MainApp().run()
import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


# layouts


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

    def __init__(self, list_of_plants, sm, **kwargs):
        super(PlantBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        button = []

        for n in range(len(list_of_plants.list)):
            button.append(Button(text=list_of_plants.list[n].common_name))
            self.add_widget(button[n])
            Manager.add_plant_screen(sm, list_of_plants.list[n])

        Manager.create_plant_screens(sm)

        for n in range(len(button)):
            button[n].bind(on_press=lambda x: Manager.switch_screens(sm, n))
            # list_of_plants.list[n]


class MainBoxes(BoxLayout):

    def __init__(self, list_of_plants, sm, **kwargs):
        super(MainBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        plant_boxes = PlantBoxes(list_of_plants, sm)
        menu_boxes = MenuBoxes()
        self.add_widget(plant_boxes)
        self.add_widget(menu_boxes)


class PlantProperties(BoxLayout):

    def __init__(self, plant, **kwargs):

        super(PlantProperties, self).__init__(**kwargs)

        self.orientation = "vertical"

        common_name_label = Label(text=plant.common_name)
        self.add_widget(common_name_label)

        botanical_name_label = Label(text=plant.botanical_name)
        self.add_widget(botanical_name_label)

        sun_exposure_label = Label(text=plant.sun_exposure)
        self.add_widget(sun_exposure_label)

        water_label = Label(text=plant.water)
        self.add_widget(water_label)

        soil_label = Label(text=plant.soil)
        self.add_widget(soil_label)

        repotting_label = Label(text=plant.repotting)
        self.add_widget(repotting_label)

        size_label = Label(text=plant.size)
        self.add_widget(size_label)


# screens


class Manager(ScreenManager):

    def __init__(self, list_of_plants, **kwargs):
        super(Manager, self).__init__(**kwargs)
        self.list = []
        self.add_widget(MenuScreen(list_of_plants, self))
        MenuScreen.name = "Menu"
        self.current = "Menu"

    def add_plant_screen(self, plant):
        self.list.append(PlantScreen(plant))

    def create_plant_screens(self):
        for n in range(len(self.list)):
            self.add_widget(self.list[n])
            self.list[n].name = ("%d" % n)

    def switch_screens(self, name):
        self.current = ("%d" % name)


class MenuScreen(Screen):

    def __init__(self, list_of_plants, sm, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        menu_page = MainBoxes(list_of_plants, sm)
        self.add_widget(menu_page)


class PlantScreen(Screen):

    def __init__(self, plant, **kwargs):
        super(PlantScreen, self).__init__(**kwargs)
        plant_page = PlantProperties(plant)
        self.add_widget(plant_page)


class MainApp(App):
    def build(self):
        from project.pickle_data import load_data
        from project.pickle_data import store_data
        from project.pickle_data import clear_file
        from project.plant_list import ListOfPlants

        self.title = "Plantopedia"

        list_of_plants = ListOfPlants()
        load_data(list_of_plants)
        clear_file()
        store_data(list_of_plants.list)

        return Manager(list_of_plants)


if __name__ == '__main__':
    MainApp().run()
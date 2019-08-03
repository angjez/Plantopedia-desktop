# main menu layouts

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from project.kivy_interface.interface_main import Manager
from kivy.uix.textinput import TextInput


class MenuBoxes(BoxLayout):
    def __init__(self, list_of_plants, sm, **kwargs):
        super(MenuBoxes, self).__init__(**kwargs)
        self.orientation = "horizontal"

        add_button = Button(text="Add", size_hint=(.1, .1))
        add_button.fbind('on_press', Manager.add_plant_screen, sm)

        delete_button = Button(text="Delete", size_hint=(.1, .1))

        edit_button = Button(text="Edit", size_hint=(.1, .1))

        for but in [add_button, delete_button, edit_button]:
            self.add_widget(but)


class PlantBoxes(BoxLayout):

    def __init__(self, list_of_plants, sm, **kwargs):
        super(PlantBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        button = []

        for n in range(len(list_of_plants.list)):
            button.append(Button(text=list_of_plants.list[n].common_name))
            self.add_widget(button[n])

        # screen manager adds all of the screens for the buttons
        Manager.push_plant_screens(sm, list_of_plants.list)

        # assigning screens to buttons
        for n in range(len(list_of_plants.list)):
            button[n].fbind('on_press', Manager.switch_screens, sm, list_of_plants.list[n].common_name)


class MainBoxes(BoxLayout):

    def __init__(self, list_of_plants, sm, **kwargs):
        super(MainBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        plant_boxes = PlantBoxes(list_of_plants, sm)
        menu_boxes = MenuBoxes(list_of_plants, sm)
        self.add_widget(plant_boxes)
        self.add_widget(menu_boxes)


# plant screen layouts


class PlantProperties(BoxLayout):

    def __init__(self, plant, sm, list_of_plants, **kwargs):
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

        menu_boxes = PlantMenuBoxes(sm, list_of_plants, plant)
        self.add_widget(menu_boxes)


class PlantMenuBoxes(BoxLayout):
    def __init__(self, sm, list_of_plants, plant, **kwargs):
        super(PlantMenuBoxes, self).__init__(**kwargs)

        from project.app.plant_list import ListOfPlants

        self.orientation = "horizontal"

        back_button = Button(text="Back", size_hint=(.1, .3))
        back_button.bind(on_press=lambda x: Manager.goto_menu(sm))

        delete_button = Button(text="Delete", size_hint=(.1, .3))

        edit_button = Button(text="Edit", size_hint=(.1, .3))

        for but in [back_button, delete_button, edit_button]:
            self.add_widget(but)


# new plant layout


class NewPlant(BoxLayout):

    def __init__(self, **kwargs):
        super(NewPlant, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(InputLabels())
        self.add_widget(Input())


class InputLabels(BoxLayout):
    def __init__(self, **kwargs):
        super(InputLabels, self).__init__(**kwargs)
        self.orientation = "vertical"

        common_name_label = Label(text="Common name: ")
        self.add_widget(common_name_label)

        botanical_name_label = Label(text="Botanical name: ")
        self.add_widget(botanical_name_label)

        sun_exposure_label = Label(text="Sun exposure: ")
        self.add_widget(sun_exposure_label)

        water_label = Label(text="Water: ")
        self.add_widget(water_label)

        soil_label = Label(text="Soil: ")
        self.add_widget(soil_label)

        repotting_label = Label(text="Repotting: ")
        self.add_widget(repotting_label)

        size_label = Label(text="Size: ")
        self.add_widget(size_label)


class Input(BoxLayout):
    def __init__(self, **kwargs):
        super(Input, self).__init__(**kwargs)
        self.orientation = "vertical"

        def on_enter(instance, value):
            print('User pressed enter in', instance)

        self.common_name_input = TextInput(multiline=False)
        self.add_widget(self.common_name_input)

        self.botanical_name_input = TextInput(multiline=False)
        self.add_widget(self.botanical_name_input)

        self.sun_exposure_input = TextInput(multiline=False)
        self.add_widget(self.sun_exposure_input)

        self.water_input = TextInput(multiline=False)
        self.add_widget(self.water_input)

        self.soil_input = TextInput(multiline=False)
        self.add_widget(self.soil_input)

        self.repotting_input = TextInput(multiline=False)
        self.add_widget(self.repotting_input)

        self.size_input = TextInput(multiline=False)
        self.add_widget(self.size_input)
        # textinput.bind(on_text_validate=on_enter)
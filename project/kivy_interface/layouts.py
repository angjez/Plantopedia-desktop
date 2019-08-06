# main menu layouts

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from project.kivy_interface.interface_main import Manager
from kivy.uix.textinput import TextInput
from project.app.plant_list import ListOfPlants
from project.app.plant_def import Plant


class MenuBoxes(BoxLayout):
    def __init__(self, list_of_plants, sm, plant_boxes, **kwargs):
        super(MenuBoxes, self).__init__(**kwargs)
        self.orientation = "horizontal"

        add_button = Button(text="Add", size_hint=(.1, .1))
        add_button.fbind('on_press', Manager.add_plant_screen, sm, list_of_plants, plant_boxes)

        delete_button = Button(text="Delete", size_hint=(.1, .1))

        edit_button = Button(text="Edit", size_hint=(.1, .1))

        for but in [add_button, delete_button, edit_button]:
            self.add_widget(but)


class PlantBoxes(BoxLayout):

    def __init__(self, **kwargs):
        super(PlantBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.button = []

    def initiate_buttons(self, list_of_plants, sm):
        for n in range(len(list_of_plants.list)):
            self.button.append(Button(text=list_of_plants.list[n].common_name))
            self.add_widget(self.button[n])

        # screen manager adds all of the screens for the buttons
        Manager.push_plant_screens(sm, list_of_plants)

        # assigning screens to buttons
        for n in range(len(list_of_plants.list)):
            self.button[n].fbind('on_press', Manager.switch_screens, sm, list_of_plants.list[n].common_name)

    def add_button(self, list_of_plants, sm):
        self.button.append(Button(text=list_of_plants.list[-1].common_name))
        self.add_widget(self.button[-1])
        self.button[-1].fbind('on_press', Manager.switch_screens, sm, list_of_plants.list[-1].common_name)


class MainBoxes(BoxLayout):

    def __init__(self, list_of_plants, sm, **kwargs):
        super(MainBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        plant_boxes = PlantBoxes()
        PlantBoxes.initiate_buttons(plant_boxes, list_of_plants, sm)
        menu_boxes = MenuBoxes(list_of_plants, sm, plant_boxes)
        self.add_widget(plant_boxes)
        self.add_widget(menu_boxes)


# plant screen layouts


class PlantProperties(BoxLayout):

    def __init__(self, plant, sm, list_of_plants, **kwargs):
        super(PlantProperties, self).__init__(**kwargs)

        self.orientation = "vertical"
        common_name_label = Label(text=plant.common_name)
        botanical_name_label = Label(text=plant.botanical_name)
        sun_exposure_label = Label(text=plant.sun_exposure)
        water_label = Label(text=plant.water)
        soil_label = Label(text=plant.soil)
        repotting_label = Label(text=plant.repotting)
        size_label = Label(text=plant.size)
        menu_boxes = PlantMenuBoxes(sm, list_of_plants)

        for label in [common_name_label, botanical_name_label, sun_exposure_label, water_label, soil_label, repotting_label, size_label, menu_boxes]:
            self.add_widget(label)


class PlantMenuBoxes(BoxLayout):
    def __init__(self, sm, list_of_plants, **kwargs):
        super(PlantMenuBoxes, self).__init__(**kwargs)

        from project.app.plant_list import ListOfPlants

        self.orientation = "horizontal"

        self.back_button = Button(text="Back", size_hint=(.1, .3))
        self.back_button.bind(on_press=lambda x: Manager.goto_menu(sm))

        self.delete_button = Button(text="Delete", size_hint=(.1, .3))
        self.delete_button.fbind('on_press', Manager.delete_plant, sm, list_of_plants)

        self.edit_button = Button(text="Edit", size_hint=(.1, .3))

        for but in [self.back_button, self.delete_button, self.edit_button]:
            self.add_widget(but)


# new plant layout


class NewPlant(BoxLayout):

    def __init__(self, list_of_plants, sm, plant_boxes,  **kwargs):
        super(NewPlant, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(InputLabels())
        self.add_widget(Input(list_of_plants, sm, plant_boxes))


class InputLabels(BoxLayout):
    def __init__(self, **kwargs):
        super(InputLabels, self).__init__(**kwargs)
        self.orientation = "vertical"

        common_name_label = Label(text="Common name: ")
        botanical_name_label = Label(text="Botanical name: ")
        sun_exposure_label = Label(text="Sun exposure: ")
        water_label = Label(text="Water: ")
        soil_label = Label(text="Soil: ")
        repotting_label = Label(text="Repotting: ")
        size_label = Label(text="Size: ")

        for label in [common_name_label, botanical_name_label, sun_exposure_label, water_label, soil_label, repotting_label, size_label]:
            self.add_widget(label)


class Input(BoxLayout):
    def __init__(self, list_of_plants, sm, plant_boxes, **kwargs):
        super(Input, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.input_fields = []
        self.collected_input = []
        self.order_tracker = []

        for n in range(0, 7):
            self.input_fields.append(TextInput(multiline=False, hint_text_color=(0, 0, 0, 0.5)))
            self.add_widget(self.input_fields[n])
            self.input_fields[n].fbind('on_text_validate', self.on_text, list_of_plants=list_of_plants, sm=sm, plant_boxes=plant_boxes)

        self.input_fields[0].hint_text = "common name"
        self.input_fields[1].hint_text = "botanical name"
        self.input_fields[2].hint_text = "sun exposure"
        self.input_fields[3].hint_text = "water"
        self.input_fields[4].hint_text = "soil"
        self.input_fields[5].hint_text = "repotting"
        self.input_fields[6].hint_text = "size"

    def on_text(self, value, list_of_plants, sm, plant_boxes):
        self.collected_input.append(value.text)
        self.order_tracker.append(value.hint_text)
        if len(self.collected_input) == 7:
            self.interpret_data(list_of_plants, sm, plant_boxes)

    def interpret_data(self, list_of_plants, sm, plant_boxes):
        from project.app.pickle_data import store_data
        from project.app.pickle_data import clear_file
        sorted_data = [None] * 7
        for n in range(len(self.order_tracker)):
            for m in range(len(self.input_fields)):
                if self.order_tracker[n] == self.input_fields[m].hint_text:
                    sorted_data[m] = self.collected_input[n]
        new_plant = Plant(sorted_data[0], sorted_data[1], sorted_data[2], sorted_data[3], sorted_data[4],
                          sorted_data[5], sorted_data[6])
        ListOfPlants.add_defined_plant(list_of_plants, new_plant)
        # the list was changed, so it's necessary to update the file
        clear_file()
        store_data(list_of_plants.list)
        sorted_data.clear()
        self.clear_input()
        PlantBoxes.add_button(plant_boxes, list_of_plants, sm)
        Manager.add_screen(sm, list_of_plants)

    def clear_input(self):
        for n in range(0, 7):
            self.input_fields[n].text = ""
        self.collected_input.clear()
        self.order_tracker.clear()

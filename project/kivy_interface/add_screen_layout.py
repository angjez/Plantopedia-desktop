from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from project.kivy_interface.interface_main import Manager
from kivy.uix.textinput import TextInput
from project.app.plant_list import ListOfPlants
from project.app.plant_def import Plant
from kivy.uix.button import Button


class InputLabel(Label):
    def on_size(self, *args):
        self.size_hint = (1.0, 1.0)
        self.halign = "left"
        self.valign = "middle"
        self.padding_x = 50
        self.bind(size=self.setter("text_size"))
        self.markup = True


class InputLabels(BoxLayout):
    def __init__(self, **kwargs):
        super(InputLabels, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (0.5, 1.0)
        self.labels = []

        self.labels.append(InputLabel(text="[b]" + "Common name: " + "[/b]"))
        self.labels.append(InputLabel(text="[b]" + "Botanical name: " + "[/b]"))
        self.labels.append(InputLabel(text="[b]" + "Sun exposure: " + "[/b]"))
        self.labels.append(InputLabel(text="[b]" + "Water: " + "[/b]"))
        self.labels.append(InputLabel(text="[b]" + "Soil: " + "[/b]"))
        self.labels.append(InputLabel(text="[b]" + "Repotting: " + "[/b]"))
        self.labels.append(InputLabel(text="[b]" + "Size: " + "[/b]"))
        self.labels.append(InputLabel(text="[b]" + "Image url: " + "[/b]"))

        for label in range(len(self.labels)):
            self.add_widget(self.labels[label])


class Input(BoxLayout):
    def __init__(self, **kwargs):
        super(Input, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.input_fields = []

        for n in range(0, 8):
            self.input_fields.append(TextInput(multiline=True, hint_text_color=(0, 0, 0, 0.5)))
            self.add_widget(self.input_fields[n])

        self.input_fields[0].hint_text = "common name"
        self.input_fields[1].hint_text = "botanical name"
        self.input_fields[2].hint_text = "sun exposure"
        self.input_fields[3].hint_text = "water"
        self.input_fields[4].hint_text = "soil"
        self.input_fields[5].hint_text = "repotting"
        self.input_fields[6].hint_text = "size"
        self.input_fields[7].hint_text = "image url"

    def interpret_data(self, list_of_plants, sm, plant_boxes, obj):
        from project.app.pickle_data import store_data
        from project.app.pickle_data import clear_file
        from project.kivy_interface.main_screen_layout import PlantBoxes

        new_plant = Plant(self.input_fields[0].text, self.input_fields[1].text, self.input_fields[2].text, self.input_fields[3].text, self.input_fields[4].text,
                          self.input_fields[5].text, self.input_fields[6].text, self.input_fields[7].text)
        ListOfPlants.add_defined_plant(list_of_plants, new_plant)
        # the list was changed, so it's necessary to update the file
        clear_file()
        store_data(list_of_plants.list)
        self.clear_input()
        PlantBoxes.add_button(plant_boxes, list_of_plants, sm)
        Manager.add_screen(sm, list_of_plants, plant_boxes)

    def clear_input(self):
        for n in range(0, 8):
            self.input_fields[n].text = ""


class AddPlantMenuBoxes(BoxLayout):
    def __init__(self, list_of_plants, sm, plant_boxes, plant_input, **kwargs):
        super(AddPlantMenuBoxes, self).__init__(**kwargs)

        self.size_hint = (1.0, 0.05)
        self.orientation = "horizontal"

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=lambda x: Manager.goto_menu(sm))

        self.confirm_button = Button(text="Confirm")
        self.confirm_button.fbind('on_press', Input.interpret_data, plant_input, list_of_plants, sm, plant_boxes)

        for but in [self.back_button, self.confirm_button]:
            self.add_widget(but)


class AddPlantHorizontal(BoxLayout):

    def __init__(self, plant_input,  **kwargs):
        super(AddPlantHorizontal, self).__init__(**kwargs)
        self.add_widget(InputLabels())
        self.add_widget(plant_input)


class AddPlantCombined(BoxLayout):

    def __init__(self, list_of_plants, sm, plant_boxes,  **kwargs):
        super(AddPlantCombined, self).__init__(**kwargs)
        plant_input = Input()
        self.add_widget(AddPlantHorizontal(plant_input))
        self.add_widget(AddPlantMenuBoxes(list_of_plants, sm, plant_boxes, plant_input))
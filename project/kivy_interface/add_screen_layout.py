from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from project.kivy_interface.interface_main import Manager
from kivy.uix.textinput import TextInput
from project.app.plant_list import ListOfPlants
from project.app.plant_def import Plant


class NewPlant(BoxLayout):

    def __init__(self, list_of_plants, sm, plant_boxes,  **kwargs):
        super(NewPlant, self).__init__(**kwargs)
        self.add_widget(InputLabels())
        self.add_widget(Input(list_of_plants, sm, plant_boxes))


class InputLabels(BoxLayout):
    def __init__(self, **kwargs):
        super(InputLabels, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (0.5, 1.0)
        self.labels = []

        self.labels.append(Label(text="[b]" + "Common name: " + "[/b]", markup=True))
        self.labels.append(Label(text="[b]" + "Botanical name: " + "[/b]", markup=True))
        self.labels.append(Label(text="[b]" + "Sun exposure: " + "[/b]", markup=True))
        self.labels.append(Label(text="[b]" + "Water: " + "[/b]", markup=True))
        self.labels.append(Label(text="[b]" + "Soil: " + "[/b]", markup=True))
        self.labels.append(Label(text="[b]" + "Repotting: " + "[/b]", markup=True))
        self.labels.append(Label(text="[b]" + "Size: " + "[/b]", markup=True))

        for label in range(len(self.labels)):
            self.labels[label].size_hint = (1.0, 1.0)
            self.labels[label].halign = "left"
            self.labels[label].valign = "middle"
            self.labels[label].padding_x = 50
            self.labels[label].bind(size=self.labels[label].setter("text_size"))
            self.add_widget(self.labels[label])


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
        from project.kivy_interface.main_screen_layout import PlantBoxes
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
        Manager.add_screen(sm, list_of_plants, plant_boxes)

    def clear_input(self):
        for n in range(0, 7):
            self.input_fields[n].text = ""
        self.collected_input.clear()
        self.order_tracker.clear()


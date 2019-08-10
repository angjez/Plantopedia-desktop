from kivy.uix.boxlayout import BoxLayout
from project.kivy_interface.interface_main import Manager
from kivy.uix.textinput import TextInput
from project.app.plant_list import ListOfPlants
from project.app.plant_def import Plant
from project.kivy_interface.add_screen_layout import InputLabels
from project.kivy_interface.main_screen_layout import PlantBoxes

class EditPlant(BoxLayout):

    def __init__(self, list_of_plants, sm, index, plant_boxes,  **kwargs):
        super(EditPlant, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(InputLabels())
        self.add_widget(EditInput(list_of_plants, sm, index, plant_boxes))


class EditInput(BoxLayout):
    def __init__(self, list_of_plants, sm, index, plant_boxes, **kwargs):
        super(EditInput, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.input_fields = []
        self.collected_input = []
        self.order_tracker = []

        for n in range(0, 7):
            self.input_fields.append(TextInput(multiline=False, hint_text_color=(0, 0, 0, 0.5)))
            self.add_widget(self.input_fields[n])
            self.input_fields[n].fbind('on_text_validate', self.on_text, list_of_plants=list_of_plants, sm=sm, index=index, plant_boxes=plant_boxes)

        self.input_fields[0].text = list_of_plants.list[index].common_name
        self.input_fields[1].text = list_of_plants.list[index].botanical_name
        self.input_fields[2].text = list_of_plants.list[index].sun_exposure
        self.input_fields[3].text = list_of_plants.list[index].water
        self.input_fields[4].text = list_of_plants.list[index].soil
        self.input_fields[5].text = list_of_plants.list[index].repotting
        self.input_fields[6].text = list_of_plants.list[index].size

        self.input_fields[0].hint_text = "common name"
        self.input_fields[1].hint_text = "botanical name"
        self.input_fields[2].hint_text = "sun exposure"
        self.input_fields[3].hint_text = "water"
        self.input_fields[4].hint_text = "soil"
        self.input_fields[5].hint_text = "repotting"
        self.input_fields[6].hint_text = "size"

    def on_text(self, value, list_of_plants, sm, index, plant_boxes):
        self.collected_input.append(value.text)
        self.order_tracker.append(value.hint_text)
        if len(self.collected_input) == 7:
            sm.remove_widget(sm.screen[index])
            PlantBoxes.remove_button(plant_boxes, index)
            ListOfPlants.delete_from_list(list_of_plants, list_of_plants.list[index].common_name)
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
        Manager.add_screen(sm, list_of_plants, plant_boxes)

    def clear_input(self):
        for n in range(0, 7):
            self.input_fields[n].text = ""
        self.collected_input.clear()
        self.order_tracker.clear()
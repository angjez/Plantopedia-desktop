from kivy.uix.boxlayout import BoxLayout
from project.kivy_interface.interface_main import Manager
from kivy.uix.textinput import TextInput
from project.app.plant_list import ListOfPlants
from project.app.plant_def import Plant
from project.kivy_interface.add_screen_layout import InputLabels
from project.kivy_interface.main_screen_layout import PlantBoxes
from kivy.uix.button import Button


class EditPlantCombined(BoxLayout):

    def __init__(self, list_of_plants, sm, index, plant_boxes,  **kwargs):
        super(EditPlantCombined, self).__init__(**kwargs)
        edit_input = EditInput(list_of_plants, index)
        self.add_widget(EditPlantHorizontal(edit_input))
        self.add_widget(EditPlantMenuBoxes(list_of_plants, sm, index, plant_boxes))


class EditPlantHorizontal(BoxLayout):

    def __init__(self, edit_input,  **kwargs):
        super(EditPlantHorizontal, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(InputLabels())
        self.add_widget(edit_input)


class EditInput(BoxLayout):
    def __init__(self, list_of_plants, index, **kwargs):
        super(EditInput, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.input_fields = []

        for n in range(0, 8):
            self.input_fields.append(TextInput(multiline=True, hint_text_color=(0, 0, 0, 0.5)))
            self.add_widget(self.input_fields[n])

        self.input_fields[0].text = list_of_plants.list[index].common_name
        self.input_fields[1].text = list_of_plants.list[index].botanical_name
        self.input_fields[2].text = list_of_plants.list[index].sun_exposure
        self.input_fields[3].text = list_of_plants.list[index].water
        self.input_fields[4].text = list_of_plants.list[index].soil
        self.input_fields[5].text = list_of_plants.list[index].repotting
        self.input_fields[6].text = list_of_plants.list[index].size
        self.input_fields[7].text = list_of_plants.list[index].image

        self.input_fields[0].hint_text = "common name"
        self.input_fields[1].hint_text = "botanical name"
        self.input_fields[2].hint_text = "sun exposure"
        self.input_fields[3].hint_text = "water"
        self.input_fields[4].hint_text = "soil"
        self.input_fields[5].hint_text = "repotting"
        self.input_fields[6].hint_text = "size"
        self.input_fields[7].hint_text = "image"

    def edited(self, list_of_plants, sm, index, plant_boxes, obj):
        sm.remove_widget(sm.screen[index])
        PlantBoxes.remove_button(plant_boxes, index)
        ListOfPlants.delete_from_list(list_of_plants, list_of_plants.list[index].common_name)
        self.interpret_data(list_of_plants, sm, plant_boxes)

    def interpret_data(self, list_of_plants, sm, plant_boxes):
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
        for n in range(0, 7):
            self.input_fields[n].text = ""


class EditPlantMenuBoxes(BoxLayout):
    def __init__(self, list_of_plants, sm, index, plant_boxes, **kwargs):
        super(EditPlantMenuBoxes, self).__init__(**kwargs)

        self.size_hint = (1.0, 0.05)
        self.orientation = "horizontal"

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=lambda x: Manager.goto_menu(sm))

        self.confirm_button = Button(text="Confirm")
        self.confirm_button.fbind('on_press', EditInput.edited, list_of_plants, sm, index, plant_boxes)

        for but in [self.back_button, self.confirm_button]:
            self.add_widget(but)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from project.kivy_interface.interface_main import Manager


class PlantProperties(BoxLayout):

    def __init__(self, plant, sm, list_of_plants, plant_boxes, **kwargs):
        super(PlantProperties, self).__init__(**kwargs)

        self.orientation = "vertical"
        common_name_label = Label(text=plant.common_name)
        botanical_name_label = Label(text=plant.botanical_name)
        sun_exposure_label = Label(text=plant.sun_exposure)
        water_label = Label(text=plant.water)
        soil_label = Label(text=plant.soil)
        repotting_label = Label(text=plant.repotting)
        size_label = Label(text=plant.size)
        menu_boxes = PlantMenuBoxes(sm, list_of_plants, plant_boxes)

        for label in [common_name_label, botanical_name_label, sun_exposure_label, water_label, soil_label, repotting_label, size_label, menu_boxes]:
            self.add_widget(label)


class PlantMenuBoxes(BoxLayout):
    def __init__(self, sm, list_of_plants, plant_boxes, **kwargs):
        super(PlantMenuBoxes, self).__init__(**kwargs)

        self.orientation = "horizontal"

        self.back_button = Button(text="Back", size_hint=(.1, .3))
        self.back_button.bind(on_press=lambda x: Manager.goto_menu(sm))

        self.delete_button = Button(text="Delete", size_hint=(.1, .3))
        self.delete_button.fbind('on_press', Manager.delete_plant, sm, list_of_plants, plant_boxes)

        self.edit_button = Button(text="Edit", size_hint=(.1, .3))
        self.edit_button.fbind('on_press', Manager.add_edit_screen, sm, list_of_plants, plant_boxes)

        for but in [self.back_button, self.delete_button, self.edit_button]:
            self.add_widget(but)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from project.kivy_interface.interface_main import Manager


class PlantProperties(BoxLayout):

    def __init__(self, plant, **kwargs):
        super(PlantProperties, self).__init__(**kwargs)

        self.labels = []

        self.labels.append(Label(text=plant.common_name, size_hint=(1.0, 1.0), halign="left", valign="middle"))
        self.labels.append(Label(text=plant.botanical_name, size_hint=(1.0, 1.0), halign="left", valign="middle"))
        self.labels.append(Label(text=plant.sun_exposure, size_hint=(1.0, 1.0), halign="left", valign="middle"))
        self.labels.append(Label(text=plant.water, size_hint=(1.0, 1.0), halign="left", valign="middle"))
        self.labels.append(Label(text=plant.soil, size_hint=(1.0, 1.0), halign="left", valign="middle"))
        self.labels.append(Label(text=plant.repotting, size_hint=(1.0, 1.0), halign="left", valign="middle"))
        self.labels.append(Label(text=plant.size, size_hint=(1.0, 1.0), halign="left", valign="middle"))

        for label in range(len(self.labels)):
            self.labels[label].bind(size=self.labels[label].setter("text_size"))
            self.add_widget(self.labels[label])


class PlantMenuBoxes(BoxLayout):
    def __init__(self, sm, list_of_plants, plant_boxes, **kwargs):
        super(PlantMenuBoxes, self).__init__(**kwargs)

        self.orientation = "horizontal"

        self.back_button = Button(text="Back", size_hint=(.1, .1))
        self.back_button.bind(on_press=lambda x: Manager.goto_menu(sm))

        self.delete_button = Button(text="Delete", size_hint=(.1, .1))
        self.delete_button.fbind('on_press', Manager.delete_plant, sm, list_of_plants, plant_boxes)

        self.edit_button = Button(text="Edit", size_hint=(.1, .1))
        self.edit_button.fbind('on_press', Manager.add_edit_screen, sm, list_of_plants, plant_boxes)

        for but in [self.back_button, self.delete_button, self.edit_button]:
            self.add_widget(but)


class CombineHorizontalBoxes(BoxLayout):
    def __init__(self, plant, **kwargs):
        super(CombineHorizontalBoxes, self).__init__(**kwargs)
        from project.kivy_interface.add_screen_layout import InputLabels

        self.add_widget(InputLabels())
        self.add_widget(PlantProperties(plant))


class CombineAllBoxes(BoxLayout):
    def __init__(self, plant, sm, list_of_plants, plant_boxes, **kwargs):
        super(CombineAllBoxes, self).__init__(**kwargs)
        menu_boxes = PlantMenuBoxes(sm, list_of_plants, plant_boxes)
        self.add_widget(CombineHorizontalBoxes(plant))
        self.add_widget(menu_boxes)

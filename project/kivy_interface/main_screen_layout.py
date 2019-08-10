from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from project.kivy_interface.interface_main import Manager


class MenuBoxes(BoxLayout):
    def __init__(self, list_of_plants, sm, plant_boxes, **kwargs):
        super(MenuBoxes, self).__init__(**kwargs)
        self.orientation = "horizontal"

        add_button = Button(text="Add", size_hint=(.1, .1))
        add_button.fbind('on_press', Manager.add_plant_screen, sm, list_of_plants, plant_boxes)

        delete_button = Button(text="Delete", size_hint=(.1, .1))
        delete_button.fbind('on_press', Manager.delete_multiple_screens, sm, list_of_plants, plant_boxes)

        for but in [add_button, delete_button]:
            self.add_widget(but)


class PlantBoxes(BoxLayout):

    def __init__(self, **kwargs):
        super(PlantBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.button = []

    def initiate_buttons(self, list_of_plants, sm, plant_boxes):
        for n in range(len(list_of_plants.list)):
            self.button.append(Button(text=list_of_plants.list[n].common_name))
            self.add_widget(self.button[n])

        # screen manager adds all of the screens for the buttons
        Manager.push_plant_screens(sm, list_of_plants, plant_boxes)

        # assigning screens to buttons
        for n in range(len(list_of_plants.list)):
            self.button[n].fbind('on_press', Manager.switch_screens, sm, list_of_plants.list[n].common_name)

    def add_button(self, list_of_plants, sm):
        self.button.append(Button(text=list_of_plants.list[-1].common_name))
        self.add_widget(self.button[-1])
        self.button[-1].fbind('on_press', Manager.switch_screens, sm, list_of_plants.list[-1].common_name)

    def remove_button(self, index):
        self.remove_widget(self.button[index])


class MainBoxes(BoxLayout):

    def __init__(self, list_of_plants, sm, **kwargs):
        super(MainBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        plant_boxes = PlantBoxes()
        PlantBoxes.initiate_buttons(plant_boxes, list_of_plants, sm, plant_boxes)
        menu_boxes = MenuBoxes(list_of_plants, sm, plant_boxes)
        self.add_widget(plant_boxes)
        self.add_widget(menu_boxes)
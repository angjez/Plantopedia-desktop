from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from project.kivy_interface.interface_main import Manager


class PlantButton(Button):
    def on_size(self, *args):
        self.size_hint = (1.0, 1.0)
        self.halign = "left"
        self.valign = "middle"
        self.padding_x = 100
        self.bind(size=self.setter("text_size"))
        self.markup = True
        self.font_size = self.height / 3


class MenuBoxes(BoxLayout):
    def __init__(self, list_of_plants, sm, plant_boxes, **kwargs):
        super(MenuBoxes, self).__init__(**kwargs)

        self.size_hint = (1.0, 0.05)

        self.add_button = Button(text="Add")
        self.add_button.fbind('on_press', Manager.add_plant_screen, sm, list_of_plants, plant_boxes)

        self.delete_button = Button(text="Delete")
        self.delete_button.fbind('on_press', Manager.delete_multiple_screens, sm, list_of_plants, plant_boxes)

        for but in [self.add_button, self.delete_button]:
            self.add_widget(but)


class PlantImages(BoxLayout):
    def __init__(self, list_of_plants, **kwargs):
        super(PlantImages, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (0.3, 1.0)
        self.spacing = 8

        self.images = []

        for n in range(len(list_of_plants.list)):
            self.images.append(AsyncImage(source=list_of_plants.list[n].image, allow_stretch=True, keep_ratio=False))
            self.add_widget(self.images[n])

    def remove_image(self, index):
        self.remove_widget(self.images[index])

    def add_image(self, list_of_plants):
        self.images.append(AsyncImage(source=list_of_plants.list[-1].image, allow_stretch=True, keep_ratio=False))
        self.add_widget(self.images[-1])


class PlantBoxes(BoxLayout):

    def __init__(self, **kwargs):
        super(PlantBoxes, self).__init__(**kwargs)
        self.button = []
        self.spacing = 8

    def initiate_buttons(self, list_of_plants, sm, plant_boxes):
        for n in range(len(list_of_plants.list)):
            self.button.append(PlantButton(text=list_of_plants.list[n].common_name))
            self.add_widget(self.button[n])

        # screen manager adds all of the screens for the buttons
        Manager.push_plant_screens(sm, list_of_plants, plant_boxes)

        # assigning screens to buttons
        for n in range(len(list_of_plants.list)):
            self.button[n].fbind('on_press', Manager.switch_screens, sm, list_of_plants.list[n].common_name)

    def add_button(self, list_of_plants, sm):
        self.button.append(PlantButton(text=list_of_plants.list[-1].common_name))
        self.add_widget(self.button[-1])
        self.button[-1].fbind('on_press', Manager.switch_screens, sm, list_of_plants.list[-1].common_name)

    def remove_button(self, name):
        for n in range(len(self.button)):
            if self.button[n].text == name:
                self.remove_widget(self.button[n])


class MainBoxes(BoxLayout):

    def __init__(self, list_of_plants, sm, **kwargs):
        super(MainBoxes, self).__init__(**kwargs)
        self.spacing = 8
        self.padding = [8, 8, 8, 8]
        plant_boxes = PlantBoxes()
        menu_boxes = MenuBoxes(list_of_plants, sm, plant_boxes)
        PlantBoxes.initiate_buttons(plant_boxes, list_of_plants, sm, plant_boxes)
        plant_boxes_and_images = BoxLayout(orientation='horizontal', padding=[8, 0, 8, 0], spacing=8)
        plant_boxes_and_images.add_widget(plant_boxes)
        plant_boxes_and_images.add_widget(PlantImages(list_of_plants))
        self.add_widget(plant_boxes_and_images)
        self.add_widget(menu_boxes)

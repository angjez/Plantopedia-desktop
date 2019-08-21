from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from project.kivy_interface.interface_main import Manager


class PlantButton(Button):
    def on_size(self, *args):
        self.size_hint = (1.0, 0.7)
        self.halign = "left"
        self.valign = "middle"
        self.padding_x = 100
        self.bind(size=self.setter("text_size"))
        self.markup = True
        self.font_size = self.height / 3
        self.background_normal = "button.png"


class Menu(BoxLayout):
    def __init__(self, list_of_plants, sm, plant_boxes, plant_images, **kwargs):
        super(Menu, self).__init__(**kwargs)

        self.add_button = Button(text="Add", background_normal = "menu_button.png")
        self.add_button.fbind('on_press', Manager.add_plant_screen, sm, list_of_plants, plant_boxes, plant_images)

        self.delete_button = Button(text="Delete", background_normal = "menu_button.png")
        self.delete_button.fbind('on_press', Manager.delete_multiple_screens, sm, list_of_plants, plant_boxes)

        for but in [self.add_button, self.delete_button]:
            self.add_widget(but)


class PlantImages(BoxLayout):
    def __init__(self, list_of_plants, **kwargs):
        super(PlantImages, self).__init__(**kwargs)
        self.size_hint = (0.3, 1.0)

        self.images = []
        self.captions = []

        for n in range(len(list_of_plants.list)):
            self.images.append(AsyncImage(source=list_of_plants.list[n].image, allow_stretch=True, keep_ratio=False))
            self.captions.append(list_of_plants.list[n].common_name)
            self.add_widget(self.images[n])

    def remove_image(self, caption):
        for n in range(len(self.captions)):
            if self.captions[n] == caption:
                self.remove_widget(self.images[n])

    def add_image(self, list_of_plants):
        self.images.append(AsyncImage(source=list_of_plants.list[-1].image, allow_stretch=True, keep_ratio=False))
        self.add_widget(self.images[-1])
        self.captions.append(list_of_plants.list[-1].common_name)


class PlantButtons(BoxLayout):
    def __init__(self, **kwargs):
        super(PlantButtons, self).__init__(**kwargs)
        self.button = []

    def initiate_buttons(self, list_of_plants, sm, plant_boxes, plant_images):
        for n in range(len(list_of_plants.list)):
            self.button.append(PlantButton(text=list_of_plants.list[n].common_name))
            self.add_widget(self.button[n])

        # screen manager adds all of the screens for the buttons
        Manager.push_plant_screens(sm, list_of_plants, plant_boxes, plant_images)

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
        plant_boxes = PlantButtons()
        plant_images = PlantImages(list_of_plants)
        menu_boxes = Menu(list_of_plants, sm, plant_boxes, plant_images)
        PlantButtons.initiate_buttons(plant_boxes, list_of_plants, sm, plant_boxes, plant_images)
        plant_boxes_and_images = BoxLayout(orientation='horizontal', padding=[8, 0, 8, 0], spacing=8)
        plant_boxes_and_images.add_widget(plant_boxes)
        plant_boxes_and_images.add_widget(plant_images)
        self.add_widget(plant_boxes_and_images)
        self.add_widget(menu_boxes)

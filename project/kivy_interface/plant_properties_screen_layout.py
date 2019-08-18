from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from project.kivy_interface.interface_main import Manager
from kivy.graphics import Color, Rectangle
from kivy.uix.image import AsyncImage


class PropertyLabelEven(Label):
    def on_size(self, *args):
        self.size_hint = (1.0, 1.0)
        self.color = (0, 0, 0, 0.65)
        self.halign = "left"
        self.valign = "middle"
        self.padding_x = 50
        self.bind(size=self.setter("text_size"))
        self.markup = True


class PropertyLabelOdd(Label):
    def on_size(self, *args):
        self.size_hint = (1.0, 1.0)
        self.color = (0, 0, 0, 0.65)
        self.halign = "left"
        self.valign = "middle"
        self.padding_x = 50
        self.markup = True
        self.bind(size=self.setter("text_size"))


class ImageCommonNameBotanicalName(BoxLayout):
    def __init__(self, plant, **kwargs):
        super(ImageCommonNameBotanicalName, self).__init__(**kwargs)
        self.size_hint = (1.0, 0.7)
        self.orientation = "horizontal"
        img = AsyncImage(source=plant.image, allow_stretch=True, keep_ratio=False)
        self.add_widget(img)

        labels_box = BoxLayout(orientation='vertical')
        labels_box.add_widget(PropertyLabelEven(text="[b]" + "Common name: " + "[/b]"))
        labels_box.add_widget(PropertyLabelOdd(text="[b]" + "Botanical name: " + "[/b]"))
        labels_box.add_widget(PropertyLabelEven(text="[b]" + "Sun exposure: " + "[/b]"))
        self.add_widget(labels_box)

        properties_labels_box = BoxLayout(orientation='vertical')
        properties_labels_box.add_widget(PropertyLabelEven(text=plant.common_name))
        properties_labels_box.add_widget(PropertyLabelOdd(text="[i]" + plant.botanical_name + "[/i]", markup = True))
        properties_labels_box.add_widget(PropertyLabelEven(text=plant.sun_exposure))
        self.add_widget(properties_labels_box)


class FeatureLabels(BoxLayout):
    def __init__(self, **kwargs):
        super(FeatureLabels, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (0.5, 1.0)
        self.labels = []

        self.labels.append(PropertyLabelOdd(text="[b]" + "Water: " + "[/b]"))
        self.labels.append(PropertyLabelEven(text="[b]" + "Soil: " + "[/b]"))
        self.labels.append(PropertyLabelOdd(text="[b]" + "Repotting: " + "[/b]"))
        self.labels.append(PropertyLabelEven(text="[b]" + "Size: " + "[/b]"))

        for label in range(len(self.labels)):
            self.add_widget(self.labels[label])


class PlantProperties(BoxLayout):

    def __init__(self, plant, **kwargs):
        super(PlantProperties, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.labels = []

        self.labels.append(PropertyLabelOdd(text=plant.water))
        self.labels.append(PropertyLabelEven(text=plant.soil))
        self.labels.append(PropertyLabelOdd(text=plant.repotting))
        self.labels.append(PropertyLabelEven(text=plant.size))

        for label in range(len(self.labels)):
            self.add_widget(self.labels[label])


class PlantMenuBoxes(BoxLayout):
    def __init__(self, sm, list_of_plants, plant_boxes, **kwargs):
        super(PlantMenuBoxes, self).__init__(**kwargs)

        self.orientation = "horizontal"
        self.size_hint = (1.0, 0.07)

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=lambda x: Manager.goto_menu(sm))

        self.delete_button = Button(text="Delete")
        self.delete_button.fbind('on_press', Manager.delete_plant, sm, list_of_plants, plant_boxes)

        self.edit_button = Button(text="Edit")
        self.edit_button.fbind('on_press', Manager.add_edit_screen, sm, list_of_plants, plant_boxes)

        for but in [self.back_button, self.delete_button, self.edit_button]:
            self.add_widget(but)


class CombineHorizontalBoxes(BoxLayout):
    def __init__(self, plant, **kwargs):
        super(CombineHorizontalBoxes, self).__init__(**kwargs)
        orientation: "horizontal"
        self.add_widget(FeatureLabels())
        self.add_widget(PlantProperties(plant))


class CombineAllBoxes(BoxLayout):
    def __init__(self, plant, sm, list_of_plants, plant_boxes, **kwargs):
        super(CombineAllBoxes, self).__init__(**kwargs)
        self.padding = [8, 8, 8, 8]
        menu_boxes = PlantMenuBoxes(sm, list_of_plants, plant_boxes)
        self.add_widget(ImageCommonNameBotanicalName(plant))
        self.add_widget(CombineHorizontalBoxes(plant))
        self.add_widget(menu_boxes)

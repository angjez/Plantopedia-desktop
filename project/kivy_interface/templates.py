from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.textinput import TextInput


Config.set('graphics', 'width', '650')
Config.set('graphics', 'height', '700')


# buttons


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
        self.background_down = "button_down.png"


class MenuButton(Button):
    def on_size(self, *args):
        self.background_normal = "menu_button.png"
        self.background_down = "button_down.png"


# labels


class PropertyLabel(Label):
    def on_size(self, *args):
        self.size_hint = (1.0, 1.0)
        self.color = (0, 0, 0, 0.65)
        self.halign = "left"
        self.valign = "middle"
        self.padding_x = 50
        self.bind(size=self.setter("text_size"))
        self.markup = True
        self.font_size = self.height / 4.5


class PlantLabel(Label):
    def on_size(self, *args):
        self.size_hint = (1.0, 1.0)
        self.color = (0, 0, 0, 0.65)
        self.halign = "left"
        self.valign = "middle"
        self.padding_x = 100
        self.bind(size=self.setter("text_size"))
        self.markup = True
        self.font_size = self.height / 3


class InputLabel(Label):
    def on_size(self, *args):
        self.size_hint = (1.0, 1.0)
        self.color = (0, 0, 0, 0.65)
        self.halign = "left"
        self.valign = "middle"
        self.padding_x = 50
        self.bind(size=self.setter("text_size"))
        self.markup = True
        self.font_size = self.height / 4


# text input
class InputField(TextInput):
    def on_size(self, *args):
        self.background_color = (0.5, 0.5, 0.5, 0.3)
        self.multiline = True
        self.hint_text_color = (0, 0, 0, 0.5)
from kivy.uix.boxlayout import BoxLayout
from project.kivy_interface.interface_main import Manager
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button


class DeleteMultipleCheckboxes(BoxLayout):
    def __init__(self, list_of_plants, **kwargs):
        super(DeleteMultipleCheckboxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.checkboxes = []
        self.active = []
        self.to_delete = []
        for n in range(len(list_of_plants.list)):
            self.checkboxes.append(CheckBox())
            self.add_widget(self.checkboxes[n])
            self.checkboxes[n].bind(active=self.on_checkbox_active)
            self.to_delete.append(None)

    def disable_checkboxes(self, sm):
        for n in range(len(self.checkboxes)):
            self.checkboxes[n].active = False
        Manager.goto_menu(sm)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.active.append(checkbox)
        else:
            self.active.remove(checkbox)

    def interpret_data(self, sm, list_of_plants, plant_boxes, del_multiple_labels):
        from project.kivy_interface.main_screen_layout import PlantBoxes
        for n in range(len(self.checkboxes)):
            for m in range(len(self.active)):
                if self.checkboxes[n] == self.active[m]:
                    Manager.delete_multiple_plants(sm, list_of_plants, plant_boxes, n)
                    self.remove_widget(self.checkboxes[n])
                    DeleteMultipleLabels.delete_label(del_multiple_labels, n)
                    PlantBoxes.remove_button(plant_boxes, del_multiple_labels.labels[n].text)
        Manager.goto_menu(sm)


class DeleteMultipleLabels(BoxLayout):
    def __init__(self, list_of_plants, **kwargs):
        super(DeleteMultipleLabels, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.labels = []
        for n in range(len(list_of_plants.list)):
            self.labels.append(Label(text=list_of_plants.list[n].common_name))
            self.add_widget(self.labels[n])

    def delete_label(self, n):
        self.remove_widget(self.labels[n])


class DeleteMultipleMenu(BoxLayout):
    def __init__(self, del_multiple_checkboxes, sm, list_of_plants, plant_boxes, del_multiple_labels, **kwargs):
        super(DeleteMultipleMenu, self).__init__(**kwargs)
        self.orientation = "horizontal"

        cancel_button = Button(text="Cancel", size_hint=(.1, .1))
        cancel_button.bind(on_press=lambda x: DeleteMultipleCheckboxes.disable_checkboxes(del_multiple_checkboxes, sm))
        delete_button = Button(text="Delete", size_hint=(.1, .1))
        delete_button.bind(on_press=lambda x: DeleteMultipleCheckboxes.interpret_data(del_multiple_checkboxes, sm, list_of_plants, plant_boxes, del_multiple_labels))

        for but in [cancel_button, delete_button]:
            self.add_widget(but)


class DeleteMultipleCombine(BoxLayout):
    def __init__(self, list_of_plants, del_multiple_checkboxes, del_multiple_labels, **kwargs):
        super(DeleteMultipleCombine, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(del_multiple_checkboxes)
        self.add_widget(del_multiple_labels)


class DeleteMultipleBoxes(BoxLayout):
    def __init__(self, list_of_plants, del_multiple_checkboxes, sm, plant_boxes, **kwargs):
        super(DeleteMultipleBoxes, self).__init__(**kwargs)
        self.orientation = "vertical"
        del_multiple_labels = DeleteMultipleLabels(list_of_plants)
        self.add_widget(DeleteMultipleCombine(list_of_plants, del_multiple_checkboxes, del_multiple_labels))
        self.add_widget(DeleteMultipleMenu(del_multiple_checkboxes, sm, list_of_plants, plant_boxes, del_multiple_labels))


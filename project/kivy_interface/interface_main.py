import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('interface_main.kv')


class Manager(ScreenManager):
    def __init__(self, list_of_plants, **kwargs):
        from project.kivy_interface.main_screen_layout import MainBoxes
        super(Manager, self).__init__(**kwargs)
        self.list = []
        self.screen = []
        self.menu_screen = Screen(name="Menu")
        self.menu_screen.add_widget(MainBoxes(list_of_plants, self))
        self.add_widget(self.menu_screen)
        self.current = "Menu"

    def push_plant_screens(self, list_of_plants, plant_boxes, plant_images):
        for n in range(len(list_of_plants.list)):
            from project.kivy_interface.plant_properties_screen_layout import CombineAllBoxes
            self.list.append(CombineAllBoxes(list_of_plants.list[n], self, list_of_plants, plant_boxes, plant_images))
            self.screen.append(Screen(name=list_of_plants.list[n].common_name))
            self.screen[n].add_widget(self.list[n])
            self.add_widget(self.screen[n])

    def switch_screens(self, name, obj):
        self.current = name

    def goto_menu(self):
        self.current = "Menu"

    def add_screen(self, list_of_plants, plant_boxes, plant_images):
        from project.kivy_interface.plant_properties_screen_layout import CombineAllBoxes
        self.screen.append(Screen(name=list_of_plants.list[-1].common_name))
        self.screen[-1].add_widget(CombineAllBoxes(list_of_plants.list[-1], self, list_of_plants, plant_boxes, plant_images))
        self.add_widget(self.screen[-1])
        self.current = list_of_plants.list[-1].common_name

    def delete_plant(self, list_of_plants, plant_boxes, plant_images, obj):
        from project.app.plant_list import ListOfPlants
        from project.kivy_interface.main_screen_layout import PlantButtons
        from project.kivy_interface.main_screen_layout import PlantImages
        from project.app.pickle_data import store_data
        from project.app.pickle_data import clear_file
        screen_to_delete = self.current
        ListOfPlants.delete_from_list(list_of_plants, screen_to_delete)
        PlantButtons.remove_button(plant_boxes, screen_to_delete)
        PlantImages.remove_image(plant_images, screen_to_delete)
        # updating the file after changing the list of plants
        clear_file()
        store_data(list_of_plants.list)
        self.goto_menu()
        self.delete_screen(screen_to_delete)

    def delete_screen(self, screen_to_delete):
        for n in range(len(self.screen)):
            if self.screen[n].name == screen_to_delete:
                screen_to_delete = self.screen[n]
                self.remove_widget(screen_to_delete)

    def delete_multiple_plants(self, list_of_plants, plant_boxes, n):
        from project.app.pickle_data import store_data
        from project.app.pickle_data import clear_file
        from project.kivy_interface.main_screen_layout import PlantButtons
        from project.app.plant_list import ListOfPlants
        ListOfPlants.delete_from_list(list_of_plants, self.screen[n].name)
        clear_file()
        store_data(list_of_plants.list)
        self.remove_widget(self.screen[n])
        PlantButtons.remove_button(plant_boxes, n)

    def delete_multiple_screens(self, list_of_plants, plant_boxes, obj):
        for n in range(len(self.screens)):
            if self.screens[n].name == "Delete multiple":
                self.remove_widget(self.screens[n])
                break
        self.add_widget(DeleteMultiple(list_of_plants, self, plant_boxes))
        DeleteMultiple.name = "Delete multiple"
        self.current = "Delete multiple"

    def add_plant_screen(self, list_of_plants, plant_boxes, plant_images, obj):
        for n in range(len(self.screens)):
            if self.screens[n].name == "Add plant":
                self.current = "Add plant"
                return 0
        self.add_widget(AddPlantScreen(self, list_of_plants, plant_boxes, plant_images))
        AddPlantScreen.name = "Add plant"
        self.current = "Add plant"

    def add_edit_screen(self, list_of_plants, plant_boxes, plant_images, obj):
        list_index = 0
        for n in range(len(list_of_plants.list)):
            if self.current == list_of_plants.list[n].common_name:
                list_index = n
        for n in range(len(self.screens)):
            if self.screens[n].name == "Edit plant":
                self.remove_widget(self.screens[n])
                break
        self.add_widget(EditPlantScreen(self, list_of_plants, list_index, plant_boxes, plant_images))
        EditPlantScreen.name = "Edit plant"
        self.current = "Edit plant"

    def refresh_add_screen(self):
        self.goto_menu()
        for screen in range(len(self.screens)):
            if self.screens[screen].name == "Add plant":
                self.remove_widget(self.screens[screen])


class AddPlantScreen(Screen):
    def __init__(self, sm, list_of_plants, plant_boxes, plant_images, **kwargs):
        super(AddPlantScreen, self).__init__(**kwargs)
        from project.kivy_interface.add_screen_layout import AddPlantCombinedLayout
        new_plant_page = AddPlantCombinedLayout(list_of_plants, sm, plant_boxes, plant_images)
        self.add_widget(new_plant_page)


class EditPlantScreen(Screen):
    def __init__(self, sm, list_of_plants, index, plant_boxes, plant_images, **kwargs):
        super(EditPlantScreen, self).__init__(**kwargs)
        from project.kivy_interface.edit_screen_layout import EditPlantCombined
        edit_plant_page = EditPlantCombined(list_of_plants, sm, index, plant_boxes, plant_images)
        self.add_widget(edit_plant_page)


class DeleteMultiple(Screen):
    def __init__(self, list_of_plants, sm, plant_boxes, **kwargs):
        super(DeleteMultiple, self).__init__(**kwargs)
        from project.kivy_interface.delete_multiple_screen_layout import DeleteMultipleBoxes
        from project.kivy_interface.delete_multiple_screen_layout import DeleteMultipleCheckboxes
        del_multiple_checkboxes = DeleteMultipleCheckboxes(list_of_plants)
        delete_multiple = DeleteMultipleBoxes(list_of_plants, del_multiple_checkboxes, sm, plant_boxes)
        self.add_widget(delete_multiple)


class MainApp(App):
    def build(self):
        from project.app.pickle_data import load_data
        from project.app.pickle_data import clear_file
        from project.app.pickle_data import store_data
        from project.app.plant_list import ListOfPlants

        self.title = "Plantopedia"
        list_of_plants = ListOfPlants()
        load_data(list_of_plants)
        clear_file()
        store_data(list_of_plants.list)

        return Manager(list_of_plants)


if __name__ == '__main__':
    MainApp().run()
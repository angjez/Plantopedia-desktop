import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        from project.pickle_data import load_data
        from project.pickle_data import store_data
        from project.pickle_data import clear_file
        from project.plant_list import ListOfPlants

        list_of_plants = ListOfPlants()
        load_data(list_of_plants)

        boxes_combined = BoxLayout(orientation='vertical')

        # horizontal boxes (menu)
        menu_box = BoxLayout(orientation='horizontal')

        add_button = Button(text="Add", size_hint=(.1, .1))
        delete_button = Button(text="Delete", size_hint=(.1, .1))
        edit_button = Button(text="Edit", size_hint=(.1, .1))
        menu_box.add_widget(add_button)
        menu_box.add_widget(delete_button)
        menu_box.add_widget(edit_button)

        # vertical boxes (plant names)
        plant_box = BoxLayout(orientation='vertical')
        button = []

        for n in range(len(list_of_plants.list)):
            button.append(Button(text=list_of_plants.list[n].common_name))
            plant_box.add_widget(button[n])

        # combining boxes together
        boxes_combined.add_widget(plant_box)
        boxes_combined.add_widget(menu_box)

        clear_file()
        store_data(list_of_plants.list)

        return boxes_combined


if __name__ == '__main__':
    MainApp().run()
import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from project.plant_list import ListOfPlants


class Main(App):

    def build(self):
        from project.pickle_data import load_data
        from project.pickle_data import store_data
        from project.pickle_data import clear_file
        from project.plant_list import ListOfPlants
        from project.plant_def import Plant

        list_of_plants = ListOfPlants()
        load_data(list_of_plants)

        plant_box = BoxLayout(orientation='vertical')
        button = []

        for n in range(len(list_of_plants.list)):
            button.append(Button(text=list_of_plants.list[n].common_name))
            plant_box.add_widget(button[n])

        clear_file()
        store_data(list_of_plants.list)

        return plant_box


if __name__ == '__main__':
    Main().run()
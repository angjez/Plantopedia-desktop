import pickle
import os
from project.plant_def import Plant
from project.plant_list import ListOfPlants


def store_data():
    filename = "plants.bin"
    outfile = open(filename, 'ab')
    for store_object in ListOfPlants.list_of_plants:
        pickle.dump(store_object.common_name, outfile)
        pickle.dump(store_object.botanical_name, outfile)
        pickle.dump(store_object.sun_exposure, outfile)
        pickle.dump(store_object.water, outfile)
        pickle.dump(store_object.soil, outfile)
        pickle.dump(store_object.repotting, outfile)
        pickle.dump(store_object.size, outfile)
    outfile.close()


def load_data():
    filename = "plants.bin"
    my_path = "./plants.bin"
    if os.path.exists(my_path) and os.path.getsize(my_path) > 0:
        infile = open(filename, 'rb')
        while True:
            try:
                common_name = pickle.load(infile)
                botanical_name = pickle.load(infile)
                sun_exposure = pickle.load(infile)
                water = pickle.load(infile)
                soil = pickle.load(infile)
                repotting = pickle.load(infile)
                size = pickle.load(infile)
                plant = Plant(common_name, botanical_name, sun_exposure, water, soil, repotting, size)
                ListOfPlants.list_of_plants.append(plant)
            except EOFError:
                break
        infile.close()


def clear_file():
    filename = "plants.bin"
    outfile = open(filename, 'wb')
    outfile.close()

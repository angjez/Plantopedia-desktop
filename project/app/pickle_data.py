import pickle
import os
from project.app.plant_def import Plant


def store_data(list_of_plants):
    filename = "plants.bin"
    outfile = open(filename, 'ab')
    for store_object in list_of_plants:
        pickle.dump(store_object.common_name, outfile)
        pickle.dump(store_object.botanical_name, outfile)
        pickle.dump(store_object.sun_exposure, outfile)
        pickle.dump(store_object.water, outfile)
        pickle.dump(store_object.soil, outfile)
        pickle.dump(store_object.repotting, outfile)
        pickle.dump(store_object.size, outfile)
        pickle.dump(store_object.image, outfile)
    outfile.close()


def load_data(list_of_plants):
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
                image = pickle.load(infile)
                plant = Plant(common_name, botanical_name, sun_exposure, water, soil, repotting, size, image)
                list_of_plants.add_defined_plant(plant)
            except EOFError:
                break
        infile.close()


def clear_file():
    filename = "plants.bin"
    outfile = open(filename, 'wb')
    outfile.close()

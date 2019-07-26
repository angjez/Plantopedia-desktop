import pickle
import os
from project.plant_def import Plants
from functools import partial


def store_data(store_object):
    filename = "plants.bin"
    outfile = open(filename, 'ab')
    pickle.dump(store_object.common_name, outfile)
    pickle.dump(store_object.botanical_name, outfile)
    pickle.dump(store_object.sun_exposure, outfile)
    pickle.dump(store_object.water, outfile)
    pickle.dump(store_object.soil, outfile)
    pickle.dump(store_object.repotting, outfile)
    pickle.dump(store_object.size, outfile)
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
                plant = Plants(common_name, botanical_name, sun_exposure, water, soil, repotting, size)
                list_of_plants.append(plant)
            except EOFError:
                break
        infile.close()

import pickle
import os
from project.plant_def import Plants


def store_data(store_object):
    filename = "plants.bin"
    outfile = open(filename, 'wb')
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
        with open(filename, "rb") as infile:
            while True:
                try:
                    restored_object = Plants(pickle.load(infile), pickle.load(infile), pickle.load(infile), pickle.load(infile), pickle.load(infile), pickle.load(infile), pickle.load(infile))
                    list_of_plants.append(restored_object)
                    store_data(restored_object)
                except EOFError:
                    break
        infile.close()

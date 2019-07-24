import pickle
from project.plant_def import Plants

filename = "plants"


def store_data (store_object):
    outfile = open(filename, 'wb')
    pickle.dump(store_object, outfile)
    outfile.close()


def load_data ():
    infile = open(filename, 'rb')
    restored_object = pickle.load(infile)
    infile.close()
    print(restored_object)

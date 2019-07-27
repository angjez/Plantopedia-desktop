class Plant:
    def __init__(self, common_name, botanical_name, sun_exposure, water, soil, repotting, size):
        self.common_name = common_name
        self.botanical_name = botanical_name
        self.sun_exposure = sun_exposure
        self.water = water
        self.soil = soil
        self.repotting = repotting
        self.size = size

    def print_variables(self):
        print("Common name: " + str(self.common_name))
        print("Botanical name: " + str(self.botanical_name))
        print("Sun exposure: " + str(self.sun_exposure))
        print("Water: " + str(self.water))
        print("Soil: " + str(self.soil))
        print("Repotting: " + str(self.repotting))
        print("Size: " + str(self.size))

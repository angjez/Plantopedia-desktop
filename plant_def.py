class Plant:
    def __init__(self, common_name, botanical_name, sun_exposure, water, soil_type, repotting, size):
        self.common_name = common_name
        self.botanical_name = botanical_name
        self.sun_exposure = sun_exposure
        self.water = water
        self.soil_type = soil_type
        self.repotting = repotting
        self.size = size
    def setDescription (self, description):
        self.description = description
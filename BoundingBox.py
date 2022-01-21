class BoundingBox:
    lat_min: float
    lat_max: float
    lon_min: float
    lon_max: float
    def __init__(self, lat_min: float, lat_max: float, lon_min: float, lon_max: float ):
        self.lat_min = lat_min
        self.lat_max = lat_max
        self.lon_min = lon_min
        self.lon_max = lon_max
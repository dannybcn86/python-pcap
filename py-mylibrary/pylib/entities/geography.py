'''
Geography Module
'''

EARTH_RADIUS = 6370

class Location:
    '''
    Class Location
    '''
    # ATRIBUTS O CAMPS A NIVELL DE CLASS (STATIC/SHARED)
    MIN_LATITUDE: float = -90.0
    MAX_LATITUDE: float = 90.0
    MIN_LONGITUDE: float = -180.0
    MAX_LONGITUDE: float = 180.0
    _counter = 0
    
    # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
    def __init__(self, latitude: float, longitude:float):
        self.latitude = latitude
        self.longitude = longitude
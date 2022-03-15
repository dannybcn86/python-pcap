'''
Geography Module
'''
import math
import random
from pylib.utils import strutils

# ATRIBUTS, VARIABLES GLOBALS O MÈTODES A NIVEL DE MÒDUL
EARTH_RADIUS = 6370

def degrees_to_dms(value: float) -> tuple[int,int,float]:
    '''Python DocString'''
    degrees = int(value)
    fminutes = abs(value -degrees) * 60
    minutes = int(fminutes)
    seconds = (fminutes - minutes) * 60
    return (degrees, minutes, seconds)

class Location:
    '''
    Class Location
    '''
    # ATRIBUTS O CAMPS A NIVELL DE CLASS (STATIC/SHARED)
    MIN_LATITUDE: float = -90.0
    MAX_LATITUDE: float = 90.0
    MIN_LONGITUDE: float = -180.0
    MAX_LONGITUDE: float = 180.0
    _counter: int = 0
    
    # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
    def __init__(self, latitude: float, longitude:float):
        Location._counter += 1
        self.latitude = latitude
        self.longitude = longitude

    @property
    def name(self):
        '''Python DocString'''
        return self._name

    @name.setter
    def name(self, value: str):
        '''Python DocString'''
        if not isinstance(value, str):
            raise TypeError("The name must be of type string.")
        self._name = value

    @property
    def latitude(self):
        '''Python DocString'''
        return self._latitude
    
    @latitude.setter
    def latitude(self, value: 'float|int'):
        '''Python DocString'''
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("The latitude must be of type float or int.")
        if value < Location.MIN_LATITUDE or value > Location.MAX_LATITUDE:
            raise ValueError(f"The latitude is out of range. Range: {Location.MIN_LATITUDE}, {Location.MAX_LATITUDE}")
        self._latitude = value

    @property
    def longitude(self):
        '''Python DocString'''
        return self._longitude

    @longitude.setter
    def longitude(self, value: 'float|int'):
        '''Python DocString'''
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("The latitude must be of type float or int.")
        if value < Location.MIN_LONGITUDE or value > Location.MAX_LONGITUDE:
            raise ValueError(f"The longitude is out of range. Range: {Location.MIN_LONGITUDE}, {Location.MAX_LONGITUDE}")
        self._longitude = value


    # Interpolations strings

    def latitude_deg(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        return f"{abs(self.latitude):.{decimals}f} {strutils.DEGREES} {'N' if self.latitude > 0 else 'S'}" if cpoint else f"{self.latitude:.{decimals}f} {strutils.DEGREES}"


    def longitude_deg(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''

        return f"{abs(self.longitude):.{decimals}f} {strutils.DEGREES} {'E' if self.longitude > 0 else 'O'}" if cpoint else f"{self.longitude:.{decimals}f} {strutils.DEGREES}"

    
    def to_degrees(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        #al return he eliminat els strutils.DEGRESS perquè ja estan al str que retorna latitude_deg i longitud_deg
        return f"{self.latitude_deg(decimals, cpoint)}  {self.longitude_deg(decimals, cpoint)}"


    # ----------------------------------------------------

    # Interpolation string + math operations

    def latitude_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        # Tuple unpaking
        (degrees, minutes, seconds) = degrees_to_dms(self.latitude)

        return f"{abs(degrees):.{decimals}f}{strutils.DEGREES} {'N' if degrees > 0 else 'S'} {abs(minutes):.{decimals}f}{strutils.PRIME} {abs(seconds):.{decimals}f}{strutils.DOUBLE_PRIME}" if cpoint else f"{degrees:.{decimals}f}{strutils.DEGREES} {minutes:.{decimals}f}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME}"


    def longitude_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        # Tuple unpacking
        (degrees, minutes, seconds) = degrees_to_dms(self.longitude)

        return f"{abs(degrees):.{decimals}f}{strutils.DEGREES} {'E' if degrees > 0 else 'O'} {abs(minutes):.{decimals}f}{strutils.PRIME} {abs(seconds):.{decimals}f}{strutils.DOUBLE_PRIME}" if cpoint else f"{degrees:.{decimals}f}{strutils.DEGREES} {minutes:.{decimals}f}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME}"


    def to_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        return f"{self.latitude_dms(decimals, cpoint)}  {self.longitude_dms(decimals, cpoint)}"
    
    # ----------------------------------------------------
    
    # Match operations

    def distance_to(self, other: 'Location') -> float:
        '''
        Python DocString
        '''
        # Tuple unpacking
        (rlat1,rlong1,rlat2,rlong2,dlat,dlong) = self._convert_radians(self, other)

        a = math.pow(math.sin(dlat/2), 2) + math.cos(rlat1) * math.cos(rlat2) * math.pow(math.sin(dlong/2), 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return EARTH_RADIUS * c


    def midpoint_to(self, other: 'Location') -> 'Location':
        '''
        Python DocString
        '''
        # Tuple unpacking
        (rlat1,rlong1,rlat2,rlong2,dlat,dlong) = self._convert_radians(self, other)

        bx = math.cos(rlat2) * math.cos(dlong)
        by = math.cos(rlat2) * math.sin(dlong)
        lat = math.degrees(math.atan2(math.sin(rlat1) + math.sin(rlat2), math.sqrt((math.cos(rlat1) + bx) ** 2 + by ** 2)))
        long = math.degrees(rlong1 + math.atan2(by, math.cos(rlat1) + bx))

        return Location(lat, long)

    # Magic Methods
    def __str__(self) -> str:
        '''Python DocString'''
        return f"{self.name} > {self.to_dms()}"

    def __eq__(self, other: 'Location') -> bool:
        '''Python DocString'''
        if not isinstance(other, Location):
            raise TypeError(f"The value to compare must be of type Location")
        
        return self.latitude == other.latitude and self.longitude == other.longitude
    
    def __ne__(self, other: 'Location') -> bool:
        '''Python DocString'''
        if not isinstance(other, Location):
            raise TypeError(f"The value to compare must be of type Location")
        return not self.__eq__(other)

    def __sub__(self, other: 'Location') -> 'Location':
        if not isinstance(other, Location):
            raise TypeError(f"The value to substract mustn't be of type Location")
        
        return self.midpoint_to(other)


    @classmethod
    def random(cls) -> 'Location': # A la versió de python 3.11 es pot definir un type hinting amb -> Self ja que és una sortida del tipus del mateix objecte
        '''Python DocString'''
        
        return Location(latitude = random.uniform(Location.MIN_LATITUDE, Location.MAX_LATITUDE), longitude = random.uniform(Location.MIN_LONGITUDE, Location.MAX_LONGITUDE))
        
        # També podem fer referència directament 'return cls()'
        # return cls(name = "", latitude = random.uniform(cls.MIN_LATITUDE, cls.MAX_LATITUDE), longitude = random.uniform(cls.MIN_LONGITUDE, cls.MAX_LONGITUDE))

    @classmethod
    def count(cls) -> int:
        '''Python DocString'''
        return cls._counter

    @staticmethod
    def _convert_radians(l1: 'Location', l2: 'Location') -> tuple[float,float,float,float,float,float]:
        rlat1 = math.radians(l1.latitude)
        rlong1 = math.radians(l1.longitude)
        rlat2 = math.radians(l2.latitude)
        rlong2 = math.radians(l2.longitude)
        dlat = rlat2 -rlat1
        dlong = rlong2 - rlong1
        return (rlat1,rlong1,rlat2,rlong2,dlat,dlong)

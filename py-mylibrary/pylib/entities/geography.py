'''
Geography Module
'''
from pylib.utils import strutils
import math

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
    _counter: int = 0
    
    # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
    def __init__(self, latitude: float, longitude:float):
        Location._counter += 1
        self.latitude = latitude
        self.longitude = longitude


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
        degrees = int(self.latitude)
        ms = (self.latitude - degrees) * 60
        minutes = int(ms)
        seconds = (ms - minutes) * 60

        return f"{abs(degrees):.{decimals}f}{strutils.DEGREES} {'N' if degrees > 0 else 'S'} {abs(minutes):.{decimals}f}{strutils.PRIME} {abs(seconds):.{decimals}f}{strutils.DOUBLE_PRIME}" if cpoint else f"{degrees:.{decimals}f}{strutils.DEGREES} {minutes:.{decimals}f}{strutils.PRIME} {seconds:.{decimals}f}{strutils.DOUBLE_PRIME}"


    def longitude_dms(self, decimals: int = 5, cpoint: bool = True) -> str:
        '''
        Python DocString
        '''
        degrees = int(self.longitude)
        ms = (self.longitude - degrees) * 60
        minutes = int(ms)
        seconds = (ms - minutes) * 60

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
        rlat1 = math.radians(self.latitude)
        rlong1 = math.radians(self.longitude)
        rlat2 = math.radians(other.latitude)
        rlong2 = math.radians(other.longitude)
        dlat = rlat2 -rlat1
        dlong = rlong2 - rlong1
        a = math.pow(math.sin(dlat/2), 2) + math.cos(rlat1) * math.cos(rlat2) * math.pow(math.sin(dlong/2), 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return EARTH_RADIUS * c


    def midpoint_to(self, other: 'Location') -> 'Location':
        '''
        Python DocString
        '''
        rlat1 = math.radians(self.latitude)
        rlong1 = math.radians(self.longitude)
        rlat2 = math.radians(other.latitude)
        rlong2 = math.radians(other.longitude)
        dlat = rlat2 -rlat1
        dlong = rlong2 - rlong1
        bx = math.cos(rlat2) * math.cos(dlong)
        by = math.cos(rlat2) * math.sin(dlong)
        lat = math.degrees(math.atan2(math.sin(rlat1) + math.sin(rlat2), math.sqrt((math.cos(rlat1) + bx) ** 2 + by ** 2)))
        long = math.degrees(rlong1 + math.atan2(by, math.cos(rlat1) + bx))

        return Location(lat, long)

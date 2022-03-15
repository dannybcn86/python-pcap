'''
Geometry Module
'''
import random
from pylib.utils import mathutils

class Color:
    '''
    Class Color
    '''
    # ATRIBUTS O CAMPS A NIVELL DE CLASS (STATIC/SHARED)
    MAX_VALUE: int = 255
    MIN_VALUE: int = 0
    _counter: int = 0
    
    # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
    def __init__(self, name: str, red: int, green: int, blue: int):
        Color._counter += 1
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue

    @property
    def name(self) -> str:
        '''Python DocString'''
        return self._name

    @name.setter
    def name(self, value: str):
        '''Python DocString'''
        if not type(value) is str:
            raise TypeError("The name must be of type string.")
        self._name = value

    @property
    def red(self) -> int:
        '''Python DocString'''
        return self._red
    
    @red.setter
    def red(self, value:int):
        '''Pyton DocString'''
        if not type(value) is int:
            raise TypeError("Red must be of type int.")
        if not Color.MIN_VALUE <= value <= Color.MAX_VALUE:
            raise ValueError("Red coordinate is out of range.")
        self._red = value

    @property
    def green(self) -> int:
        '''Python DocString'''
        return self._green
    
    @green.setter
    def green(self, value:int):
        '''Pyton DocString'''
        if not type(value) is int:
            raise TypeError("Green must be of type int.")
        if not Color.MIN_VALUE <= value <= Color.MAX_VALUE:
            raise ValueError("Green coordinate is out of range.")
        self._green = value

    @property
    def blue(self) -> int:
        '''Python DocString'''
        return self._blue
    
    @blue.setter
    def blue(self, value:int):
        '''Pyton DocString'''
        if not type(value) is int:
            raise TypeError("Blue must be of type int.")
        if not Color.MIN_VALUE <= value <= Color.MAX_VALUE:
            raise ValueError("Blue coordinate is out of range.")
        self._blue = value

    # Magic Methods
    def __str__(self) -> str:
        '''Python DocString'''
        return f"{self.name} > {self.to_hex()}"

    def __eq__(self, other: 'Color') -> bool:
        '''Python DocString'''
        if not isinstance(other, Color):
            raise TypeError(f"The value to compare must be of type Color")
        
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __ne__(self, other: 'Color') -> bool:
        '''Python DocString'''
        if not isinstance(other, Color):
            raise TypeError(f"The value to compare mustn't be of type Color")
        return not self.__eq__(other)

    # COMPORTAMENT: METODES/OPERACIONS A NIVELL D'OBJECTE O INSTANCIA
    def to_hex(self, upper:bool = True) -> str:
        '''Python DocString'''
        return f"#{self.red:02X}{self.green:02X}{self.blue:02X}" if upper else f"#{self.red:02x}{self.green:02x}{self.blue:02x}"

    def to_rgb(self) -> str:
        '''Python DocString'''
        return f"RGB({self.red}, {self.green}, {self.blue})"

    # METODES/OPERACIONS A NIVELL DE CLASS
    @classmethod
    def random(cls) -> 'Color':
        '''Python DocString'''
        return cls(name = "", red = random.randint(cls.MIN_VALUE, cls.MAX_VALUE), green = random.randint(cls.MIN_VALUE, cls.MAX_VALUE), blue = random.randint(cls.MIN_VALUE, cls.MAX_VALUE))
        # return Color(red = random.uniform(Color.MIN_VALUE, Color.MAX_VALUE), green = random.uniform(Color.MIN_VALUE, Color.MAX_VALUE), blue = random.uniform(Color.MIN_VALUE, Color.MAX_VALUE))
    
    @classmethod
    def from_hex(cls, text: str) -> 'Color':
        '''Python DocString'''
        return cls(name = f"Color {text}", red = int(text[1:3],base = mathutils.BASE_HEX), green = int(text[3:5], base = mathutils.BASE_HEX), blue = int(text[5:7], base = mathutils.BASE_HEX))

    @classmethod
    def counter(cls) -> int:
        return cls._counter

'''
Geometry Module
'''
import random

from numpy import greater_equal
from pylib.utils import mathutils

DEFAULT_BG_COLOR = "#CCCCCC"

class Color(object):
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

class AlphaColor(Color):
    '''Class AlphaColor'''
    # ATRIBUTS O CAMPS A NIVELL DE CLASS (STATIC/SHARED)
    MIN_ALPHA = 0
    MAX_ALPHA = 100
    
    def __init__(self, name: str, red: int, green: int, blue: int, alpha: int):
        # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
        super().__init__(name, red, green, blue)
        self._alpha = alpha
        
    @property
    def alpha(self) ->int:
        return self._alpha
    
    @alpha.setter
    def alpha(self, value: int) -> int:
        if not isinstance(value, int):
            raise TypeError("The alpha must be of type integer.")
        if not AlphaColor.MIN_ALPHA <= value <= AlphaColor.MAX_ALPHA:
            raise ValueError(f"Alpha coordinate is out of range. MIN_ALPHA: {AlphaColor.MIN_ALPHA} - MAX_ALPHA: {AlphaColor.MAX_VALUE}")

    def to_hex(self, upper: bool = True) -> str:
        '''Python DocString'''
        return f"{super().to_hex(upper)} - A: {self.alpha}%"
    
    def to_rgb(self) -> str:
        '''Python DocString'''
        return f"{super().to_rgb()} - A: {self.alpha}%"

from abc import ABC, abstractmethod

class Shape(ABC):
    '''Python DocString'''
    def __init__(self, background_color: 'Color', fore_color: 'Color') -> None:
        self.background_color = background_color
        self.fore_color = fore_color

    @abstractmethod # Per obligar a que una class que hereti les característiques d'aquesta class hagi de reeditar aquest mètode 'area()'
    def area(self):
        '''Python DocString'''
        return
        # raise NotImplementedError("Not implemented")
    
    @abstractmethod
    def perimeter(self) -> float:
        return

    @abstractmethod
    def volume(self) -> float:
        return

class Square(Shape):
    '''Python DocString'''
    def __init__(self, side: float|int, background_color: 'Color' = Color.from_hex("#CCCCCC"), fore_color: 'Color' = Color.from_hex("#BBBBBB")) -> None:
        super().__init__(background_color, fore_color)
        self.side = side

    @property
    def side(self) -> float|int:
        return self._side

    @side.setter
    def side(self, value) -> float|int:
        self._side = value

class Rectangle(Shape):
    '''Python DocString'''
    pass

class Triangle(Shape):
    '''Python DocString'''
    pass
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

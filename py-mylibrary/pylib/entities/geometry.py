'''
Geometry Module
'''

class Color:
    '''
    Class Color
    '''
    # ATRIBUTS O CAMPS A NIVELL DE CLASS (STATIC/SHARED)
    _counter: int = 0
    
    # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
    def __init__(self, name: str, red: int, green: int, blue: int):
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue
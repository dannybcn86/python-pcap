'''
Math Utilities
'''
import builtins
import math

# ATRIBUTS O VARIABLES GLOBALS A NIVELL DE MÒDUL
PI:float = 3.141592653589793
E:float = 2.718281828459045
PHI:float = (1 + math.sqrt(5))/2 # 1618033988749894...

# Retornem el valor absolut on a la entrada notem que el valor que esperem és un número sencer o flotant (int|float) i la devolució esperada (-> int|float) tot i que no forcem res sinó que és informatiu [Type Hint]
def abs(value: int|float) -> int|float:
    '''
    Calculate absolute value of given parameter |-op| = op
    '''
    return value if value >= 0 else -value

# Número parell on a la entrada notem que el valor que esperem és un número sencer (int) i la devolució esperada (-> bool) tot i que no forcem res sinó que és informatiu [Type Hint]
def is_even(value: int) -> bool:
    '''
    Return True if given value if an even number, else return False
    '''
    return value % 2 == 0

# Número senar on a la entrada notem que el valor que esperem és un número sencer (int) i la devolució esperada (-> bool) tot i que no forcem res sinó que és informatiu [Type Hint]
def is_odd(value: int) -> bool:
    '''
    Return True if given value if an odd number, else return False
    '''
    return value % 2 != 0

elevar = lambda x:x**2

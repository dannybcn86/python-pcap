'''
Staff Module
'''

from datetime import date
import math
from pylib.utils import strutils


class Employee:
    '''
    Class Employee
    '''
    # ATRIBUTS O CAMPS A NIVELL DE CLASS (STATIC/SHARED)
    DEFAULT_SALARY: float = 1200.0
    DEFAULT_PAYMENTS: int = 12
    _counter: int = 0

    # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
    # Magic Method __init__ (Dunders)
    def __init__(self, firstname: str, lastname: str, birthdate: date, height: float, weight: float, monthly_salary: float = DEFAULT_SALARY, payments: int = DEFAULT_PAYMENTS):
        '''
        Definim el nostre inicialitzador d'objecte
        '''
        # ---> []object > Inicialitzar l'estat d'aquest objecte
        # Inicialitzem els atributs o camps d'instància o objecte (self.XXX)
        Employee._counter += 1
        self.code = f"E{Employee._counter:03d}"
        self.fistname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.height = height
        self.weight = weight
        self.monthly_salary = monthly_salary
        self.payments = payments

    # COMPORTAMENT: MÈTODES/OPERACIONS A NIVELL D'OBJECTE O INSTÀNCIA
    def fullname(self) -> str:
        ''' Python DocString '''
        return f"{self.fistname} {self.lastname}"

    def reverse_name(self) -> str:
        ''' Python DocString '''
        return f"{self.lastname}, {self.fistname}"

    def age(self) -> int:
        ''' Python DocString '''
        # fecha actual - fecha del nacimiento
        interval =  date.today() - self.birthdate
        
        return math.floor(interval.days/365)

    def bmi(self) -> tuple[float|str]:
        ''' Python DocString '''
        bmi = self.weight / math.pow(self.height, 2)
        status = strutils.EMPTY

        if bmi < 18.5:
            status = "Underweight"
        elif bmi >= 18.5 and bmi <= 24.9:
            status = "Normal weight"
        elif bmi >= 25.0 and bmi <= 29.9:
            status = "Overweight"
        elif bmi >= 30.0 and bmi <= 34.9:
            status = "Obesity class I"
        elif bmi >= 35.0 and bmi <= 39.9:
            status = "Obesity class II"
        elif bmi > 40.0:
            status = "Obesity class III"
        
        return (bmi, status)
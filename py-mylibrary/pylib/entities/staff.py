'''
Staff Module
'''

from datetime import date
import math
from pylib.utils import strutils


class Employee(object):
    '''
    Class Employee
    '''
    # ATRIBUTS O CAMPS A NIVELL DE CLASS (STATIC/SHARED)
    DEFAULT_SALARY: float = 1200.0
    DEFAULT_PAYMENTS: int = 12
    _counter: int = 0

    # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
    # Magic Method __init__ (Dunders)
    def __init__(self, firstname: str, lastname: str, birthdate: date, height: float, weight: float, hiredate : date = date.today(), monthly_salary: float = DEFAULT_SALARY, payments: int = DEFAULT_PAYMENTS):
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
        self.hiredate = hiredate
        self.monthly_salary = monthly_salary
        self.payments = payments

    # COMPORTAMENT: MÈTODES/OPERACIONS A NIVELL D'OBJECTE O INSTÀNCIA
    def fullname(self) -> str:
        ''' Retorna el nom complet del empleat '''
        return f"{self.fistname} {self.lastname}"

    def reverse_name(self) -> str:
        ''' Retorna el nom complet amb el format <lastname>,<firstname> del empleat '''
        return f"{self.lastname}, {self.fistname}"

    def age(self) -> int:
        ''' Retorna edat del empleat '''
        # fecha actual - fecha del nacimiento
        interval =  date.today() - self.birthdate
        return math.floor(interval.days/365)

    def seniority(self) -> int:
        '''Python DocString'''
        interval = date.today() - self.hiredate # D'una operació amb dates obtenim un objecte de tipus timedelta
        return interval.days
        # raise NotImplementedError("Error no implementado aún!")

    def bmi(self) -> tuple[float|str]:
        ''' Retorna el bmi del empleat '''
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

    def annual_salary(self) -> float:
        '''Python DocString'''
        return self.monthly_salary * self.payments

    # Magic Methods
    def __str__(self) -> str:
        return f"{self.code} > {self.fullname}"

    def __len__(self) -> int:
        '''Python String'''
        return self.seniority()
 
    def __lt__(self, other: 'Employee') -> bool:
        '''Pyton DocString'''
        if not isinstance(other, Employee):
            raise TypeError("You can only compare with another Employee")
        return self.age() < other.age()
    
    def __le__(self, other: 'Employee') -> bool:
        '''Pyton DocString'''
        if not isinstance(other, Employee):
            raise TypeError("You can only compare with another Employee")
        return self.age() <= other.age()
    
    def __gt__(self, other: 'Employee') -> bool:
        '''Pyton DocString'''
        if not isinstance(other, Employee):
            raise TypeError("You can only compare with another Employee")
        return self.age() > other.age()

    def __ge__(self, other: 'Employee') -> bool:
        '''Pyton DocString'''
        if not isinstance(other, Employee):
            raise TypeError("You can only compare with another Employee")
        return self.age() >= other.age()

    def __add__(self, value: int|float):
        '''Python DocString'''
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("You can only operate with int or float object type")
        self.monthly_salary += value

    def __sub__(self, value: int|float):
        '''Python DocString'''
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("You can only operate with int or float object type")
        self.monthly_salary -= value
        
    
    def __mul__(self, value: int|float):
        '''Python DocString'''
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("You can only operate with int or float object type")
        self.monthly_salary *= value
        

    def __truediv__(self, value: int|float):
        '''Python DocString'''
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("You can only operate with int or float object type")
        self.monthly_salary /= value

    def __del__(self):
        '''Python DocString'''
        print("-" * 100)
        print(f"Estoy muriendome --> {self.__str__()}") # Es igual que hacer lo siguiente: print(f"Estoy muriendome --> {str(self)}")
        print("-" * 100)


class SalesEmployee(Employee):
    '''Class SalesEmployee'''
    # ATRIBUTS O CAMPS A NIVELL DE CLASS (STATIC/SHARED)
    DEFULT_COMMISSION: float = 3000

    # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
    # Magic Method __init__ (Dunders)
    # def __init__(self, commission: float = DEFULT_COMMISSION):
    def __init__(self, firstname: str, lastname: str, birthdate: date, height: float, weight: float, hiredate: date = date.today(), monthly_salary: float = Employee.DEFAULT_SALARY, payments: int = Employee.DEFAULT_PAYMENTS, commission: float = DEFULT_COMMISSION):
        '''
        Definim el nostre inicialitzador d'objecte
        '''
        super().__init__(firstname, lastname, birthdate, height, weight, hiredate, monthly_salary, payments)
        # Inicialitzem els atributs o camps d'instància o objecte (self.XXX)
        self.commission = commission
    
    @property
    def commission(self) -> float:
        return self._commission
    
    @commission.setter
    def commission(self, value):
        self._commission = value

    def annual_salary(self) -> float:
        '''Python DocString'''
        print("-->Soy un comercial y he redefinido esta operación")
        return super().annual_salary() + self.commission
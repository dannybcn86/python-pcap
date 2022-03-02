'''
Main Module
'''
from datetime import date
from pylib.utils import mathutils           # import pylib.utils.mathutils as mathutils
from pylib.utils import strutils            # import pylib.utils.strutils as strutils
from pylib.utils import sysutils            # import pylib.utils.sysutils as sysutils
from pylib.entities import geography        # import pylib.entities.geography as geography
from pylib.entities import geometry         # import pylib.entities.geometry as geometry
from pylib.entities import planning         # import pylib.entities.planning as planning
from pylib.entities import staff            # import pylib.entities.staff as staff

from pylib.entities.geography import Location
from pylib.entities.staff import Employee
from pylib.entities.geometry import Color



# Definició del mòdul principal main()
def main():
    '''
    Main Function
    '''
    print("*" * 100)
    # Mostrem el magic method __name__ del mòdul mathutils i els valors de les seves constants (magic numbers)
    print(f"Modulo: {mathutils.__name__}")
    print("*" * 100)
    print(f"PI = {mathutils.PI:.3f}")
    print(f"E = {mathutils.E:.3f}")
    print(f"PHI = {mathutils.PHI:.3f}")

    # Mostrem el magic method __name__ del mòdul geography i els valors de les seves constants (magic numbers)
    print("*" * 100)
    print(f"Modulo: {geography.__name__}")
    print("*" * 100)
    print(f"EARTH_RADIUS = {geography.EARTH_RADIUS} km")

    # Mostrem el magic method __name__ del mòdul strutils i els valors de les seves constants unicode (magic letters)
    print("*" * 100)
    print(f"Modulo: {strutils.__name__}")
    print("*" * 100)
    print(f"DEGREES = {strutils.DEGREES}")
    print(f"DEGREES_CELSIUS = {strutils.DEGREES_CELSIUS}")
    print(f"DEGREES_FAHRENHEIT = {strutils.DEGREES_FAHRENHEIT}")
    print(f"PRIME = {strutils.PRIME}")
    print(f"DOUBLE_PRIME = {strutils.DOBULE_PRIME}")

    for i in range(20):
        print(f"{i:02d} => Even: {mathutils.is_even(i)} || Odd: {mathutils.is_odd(i)}")

    print("*" * 100)
    print(f"Module: {planning.__name__}")
    print("*" * 100)
    print(f"CURRENT YEAR = {planning.current_year()}")
    print(f"ELAPSED DAYS = {planning.elapsed_days()}")
    print(f"REMAINING DAYS = {planning.remaining_days()}")
    print(f"IS LEAP YEAR = {planning.is_leap_year()}")
    print(f"TOTAL DAYS = {planning.total_days()}")
    print(f"PREV LEAP YEAR = {planning.prev_leap_year()}")
    print(f"NEXT LEAP YEAR = {planning.next_leap_year()}")
    print(f"YEAR PROGRESS OF 2020 = {planning.year_progress(pretty=False,year=2020)}")
    print(f"YEAR PROGRESS WITHOUT PRETTY MODE = {planning.year_progress(pretty=False)}")
    print(f"YEAR PROGRESS WITH PRETTY MODE = {planning.year_progress(2020)}")


    print(strutils.truncate(text = "Hola que tal estas, a ver si truncaas", max_length = 40))
    print(strutils.truncate(text = "Hola que tal estas, a ver si truncaas", max_length = 20))
    print(strutils.truncate(text = "Hola que tal estas, a ver si truncaas", max_length = 20, placeholder = "[...]"))

    for i in range(10):
        print("*" * 150)
        print(F"Code: {strutils.randcode()}")
        print(F"Code: {strutils.randcode(length = 12, punctuation=False)}")
        print(F"Code: {strutils.randcode(length = 12, uppercase_letters=True, lowercase_letters = True, digits=False, punctuation=False)}")
        print("*" * 150)

    
    my_codes = strutils.randcodes(num_codes=100, length=12)
    print(f"Codes: {len(my_codes)}")
    print(my_codes)
    print(my_codes[0:2])
    print(my_codes[-1])

    print(F"DEFAULT_SALARY: {Employee.DEFAULT_SALARY} €")
    print(F"DEFAULT_PAYMENTS: {Employee.DEFAULT_PAYMENTS}")
    print(F"Counter: {Employee._counter}")
    e1 = Employee(firstname = "Jordi", lastname = "Ariño", birthdate = date(year = 1980, month = 10, day = 23), height = 1.86, weight = 80)
    e2 = Employee(firstname = "Ramon", lastname = "Carles", birthdate = date(year = 1980, month = 10, day = 23), height = 1.76, weight = 85)
    e3 = Employee(firstname = "Elisabet", lastname = "Castro", birthdate = date(year = 1980, month = 10, day = 23), height = 1.80, weight = 90)
    e4 = Employee(firstname = "Enrique", lastname = "Ramirez", birthdate = date(year = 1980, month = 10, day = 23), height = 1.70, weight = 75)
    e5 = Employee(firstname = "Jordi", lastname = "Alejandro", birthdate = date(year = 1980, month = 10, day = 23), height = 1.90, weight = 95)
    employees = [e1,e2,e3,e4,e5]
    for employee in employees:
        print("-" * 150)
        print(F"Code: {employee.code}")
        print(F"First Name: {employee.fistname}")
        print(F"Last Name: {employee.lastname}")
        print(F"Birthdate: {employee.birthdate}")
        print(F"Monthly Salary: {employee.monthly_salary}")
        print(F"Payments: {employee.payments}")
        print("-" * 150)
        print(F"Fullname: {employee.fullname()}")
        print(F"Reversename: {employee.reverse_name()}")
        print(F"Age: {employee.age()} years")
        print(F"BMI: {employee.bmi()}")
        print("-" * 150)

    print(F"Latitude: ({Location.MIN_LATITUDE:+},{Location.MAX_LATITUDE:+})")
    print(F"Longitude: ({Location.MIN_LONGITUDE:+},{Location.MAX_LONGITUDE:+})")
    print(F"Counter: {Location._counter}")
    l1 = Location(latitude = 0.0, longitude = 0.0)
    l2 = Location(latitude = 0.0, longitude = 0.0)
    l3 = Location(latitude = 0.0, longitude = 0.0)
    l4 = Location(latitude = 0.0, longitude = 0.0)
    l5 = Location(latitude = 0.0, longitude = 0.0)
    locations = [l1,l2,l3,l4,l5]

    c1 = Color(name = "Black", red = 0, green = 0, blue = 0)
    c2 = Color(name = "White", red = 255, green = 255, blue = 255)
    c3 = Color(name = "Black", red = 0, green = 0, blue = 0)
    c4 = Color(name = "Black", red = 0, green = 0, blue = 0)
    c5 = Color(name = "White", red = 255, green = 255, blue = 255)
    colors = [c1,c2,c3,c4,c5]



if __name__ == "__main__":
    main()
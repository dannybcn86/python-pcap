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
from pylib.entities.staff import Employee, SalesEmployee
from pylib.entities.geometry import Color, AlphaColor, Shape, Square, Rectangle, Triangle

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
    print(f"DOUBLE_PRIME = {strutils.DOUBLE_PRIME}")

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

    ############################################################################################################
    # Crides a la class Employee del mòdul pylib.entities.staff
    ############################################################################################################
    print(F"DEFAULT_SALARY: {Employee.DEFAULT_SALARY} €")
    print(F"DEFAULT_PAYMENTS: {Employee.DEFAULT_PAYMENTS}")
    print(F"Counter: {Employee._counter}")
    e1 = Employee(firstname = "Jordi", lastname = "Ariño", birthdate = date(year = 1980, month = 10, day = 23), height = 1.86, weight = 80, hiredate = date(year = 2022, month = 3, day = 1 ))
    e2 = Employee(firstname = "Ramon", lastname = "Carles", birthdate = date(year = 1980, month = 10, day = 23), height = 1.76, weight = 85, hiredate = date(year = 2022, month = 3, day = 9 ))
    e3 = Employee(firstname = "Elisabet", lastname = "Castro", birthdate = date(year = 1980, month = 10, day = 23), height = 1.80, weight = 90)
    e4 = Employee(firstname = "Enrique", lastname = "Ramirez", birthdate = date(year = 1980, month = 10, day = 23), height = 1.70, weight = 75)
    e5 = Employee(firstname = "Jordi", lastname = "Alejandro", birthdate = date(year = 1980, month = 10, day = 23), height = 1.90, weight = 95)
    e6 = SalesEmployee(firstname = "Jordi", lastname = "Alejandro", birthdate = date(year = 1980, month = 10, day = 23), height = 1.90, weight = 95, commission = 5000)

    employees = (e1,e2,e3,e4,e5,e6)
    for employee in employees:
        print("-" * 150)
        print(F"Code: {employee.code}")
        print(F"First Name: {employee.fistname}")
        print(F"Last Name: {employee.lastname}")
        print(F"Birthdate: {employee.birthdate}")
        print(F"Monthly Salary: {employee.monthly_salary}")
        print(F"Payments: {employee.payments}")
        print(F"Seniority: {employee.seniority()}")
        print("-" * 150)
        print(F"Fullname: {employee.fullname()}")
        print(F"Reversename: {employee.reverse_name()}")
        print(F"Age: {employee.age()} years")
        print(F"BMI: {employee.bmi()}")
        print(F"Annual Salary: {employee.annual_salary()}")
        print("-" * 150)
    
    # Comparativa amb els magic methods __lt__, __le__, __gt__, __ge__
    print("*" * 150)
    print("Comparamos empleados e1 y e2")
    print("*" * 150)
    print(e1 > e2)
    print(e1 < e2)
    print(e1 >= e2)
    print(e1 <= e2)
    print(len(e1))
    # Modifiquem el sou del empleat fent les següents operacions i reescribim el seu sou
    e1 * 5
    e1 + 100
    e1 - 100
    e1 / 5
    print("*" * 150)
    ############################################################################################################

    ############################################################################################################
    # Crides a la class Location del mòdul pylib.entities.geography
    ############################################################################################################
    print(F"Latitude: ({Location.MIN_LATITUDE:+},{Location.MAX_LATITUDE:+})")
    print(F"Longitude: ({Location.MIN_LONGITUDE:+},{Location.MAX_LONGITUDE:+})")
    print(F"Counter: {Location._counter}")
    mad = Location(latitude = 40.4165, longitude = -3.7035825)
    bcn = Location(latitude = 41.3828939, longitude = 2.1774322)
    paris = Location(latitude = 48.8588897, longitude = 2.320041)
    ny = Location(latitude = 40.7127281, longitude = -74.0060152)
    london = Location(latitude = 51.5073219, longitude = -0.1276474)
    prnd1 = Location.random()
    prnd2 = Location.random()
    locations = (mad,bcn,paris,ny,london, prnd1, prnd2)

    for location in locations:
        print("-" * 150)
        print(f"Latitude: {location.latitude_deg(decimals = 3, cpoint = False)}")
        print(f"Longitude: {location.longitude_deg(decimals = 3, cpoint = False)}")
        print(f"Latitude cpoint: {location.latitude_deg(decimals = 3)}")
        print(f"Longitude cpoint: {location.longitude_deg(decimals = 3)}")
        print(f"Coordenate deg: {location.to_degrees(decimals = 3, cpoint = False)}")
        print(f"Coordenate deg cpoint: {location.to_degrees(decimals = 3)}")
        print("-" * 150)
        print(f"Latitude dms: {location.latitude_dms(decimals = 4, cpoint = False)}")
        print(f"Logitude dms: {location.longitude_dms(decimals = 4, cpoint = False)}")
        print(f"Latitude dms cpoint: {location.latitude_dms(decimals = 4)}")
        print(f"Logitude dms cpoint: {location.longitude_dms(decimals = 4)}")
        print(f"Coordenate dms: {location.to_dms(decimals = 3, cpoint = False)}")
        print(f"Coordenate dms cpoint: {location.to_dms(decimals = 3)}")
        print("-" * 150)

    print(f"BCN-MAD: {bcn.distance_to(mad)} Km")
    print(f"BCN-NY: {bcn.distance_to(ny)} Km")
    print(f"BCN-LONDON: {bcn.distance_to(london)} Km")
    print("*" * 150)
    print(f"BCN-MAD: {bcn.midpoint_to(mad).to_degrees()}")
    print(f"BCN-NY: {bcn.midpoint_to(ny).to_degrees()}")
    print(f"BCN-PARIS: {bcn.midpoint_to(paris).to_degrees()}")

    print(f"Count: {Location.count()}")
    ############################################################################################################

    ############################################################################################################
    # Crides a la class Color del mòdul pylib.entities.geometry
    ############################################################################################################
    c1 = Color(name = "Black", red = 0, green = 0, blue = 0)
    c2 = Color(name = "White", red = 255, green = 255, blue = 255)
    c3 = Color(name = "Black", red = 0, green = 0, blue = 0)
    c4 = Color(name = "Black", red = 0, green = 0, blue = 0)
    c5 = Color(name = "White", red = 255, green = 255, blue = 255)
    c6 = Color.random() 
    c7 = Color.random()
    c8 = Color.from_hex("#FF0000")
    c9 = Color.from_hex("#008000")
    c10 = Color(name= "My color 1", red = 0, green = 25, blue = 75)
    c11 = Color(name= "My color 2", red = 0, green = 25, blue = 75)
    c12 = AlphaColor(name = "My AlphaColor", red = 50, green = 90, blue = 99, alpha = 50)
    
    print("*" * 150)
    print("*" * 150)
    c1.red = 250 # Accedim a l'objecte en mode setter
    coord = Location(latitude = 90.0, longitude = 180.0)
    print(vars(c1)) # Accedim a l'objecte en mode getter
    print("*" * 150)
    print("*" * 150)
    
    colors = (c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12)

    for color in colors:
        print("-" * 150)
        print(f"Color: {color.to_hex()}")
        print(f"Color: {color.to_rgb()}")
        print("-" * 150)
    
    figure = Shape(c8, c9)
    ############################################################################################################

if __name__ == "__main__":
    main()
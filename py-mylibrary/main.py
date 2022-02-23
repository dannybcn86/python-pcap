'''
Main Module
'''
import geography
import geometry
import mathutils
import planning
import strutils
import sysutils


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
if __name__ == "__main__":
    main()
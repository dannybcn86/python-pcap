'''
Main Module
'''

import pyconvert as pc

# Constants unicode
DEGREES_CELSIUS = "\u2103"
DEGREES_FAHRENHEIT = "\u2109"

def main():
    '''
    This is the main module
    '''
    print("*" * 100)
    print("CONVERSIÓN DE TEMPERATURAS")
    print("*" * 100)
    celsius=float(input(f"Introduce tu temperatura celsius {DEGREES_CELSIUS}  para convertir a fahrenheit {DEGREES_FAHRENHEIT} : "))
    print("-" * 100)
    print(f"Celsius: {celsius}{DEGREES_CELSIUS}, Fahrenheit: {pc.to_fahrenheit(temp = celsius)}{DEGREES_FAHRENHEIT}")
    print("*" * 100)
    fahrenheit=float(input(f"Introduce tu temperatura fahrenheit {DEGREES_FAHRENHEIT}  para convertir a celsius {DEGREES_CELSIUS} : "))
    print("-" * 100)
    print(f"Fahrenheit: {fahrenheit}{DEGREES_FAHRENHEIT}, Celsius: {pc.to_celsius(temp = fahrenheit)}{DEGREES_CELSIUS}")
    print("*" * 100)
    print()
    print("*" * 100)
    print("CONVERSIÓN DE DISTANCIAS")
    print("*" * 100)
    kilometers=float(input(f"Introduce tu valor en km para convertir a pulgadas, pies y yardas:"))
    print("-" * 100)
    print(f"Kilometers: {kilometers}, pulgadas: {pc.to_inches(kilometers)}, pies: {pc.to_feets(kilometers)}, yardas: {pc.to_yards(kilometers)}")
    print("*" * 100)
    print()
    print("*" * 100)
    print("CÁLCULO DEL BMI")
    print("*" * 100)
    weightvalue=float(input(f"Introduce tu peso en kg: "))
    heightvalue=float(input(f"Introduce tu altura en metros: "))
    print("-" * 100)
    print(f"El valor de tu BMI con tus valores de peso {weightvalue} y altura {heightvalue} es de: {pc.bmi(weight = weightvalue,height = heightvalue, pretty = False)}")
    print("*" * 100)

if __name__ == "__main__":
    main()
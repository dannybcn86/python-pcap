'''
PyConvert Module
'''

import string

# Constants
EMPTY:str = ""
INCHES:float = 39370.07874
FEETS:float = 3280.839895
YARDS:float = 1093.613298

# Inicialització de variables
celsius:float = 0.0
fahrenheit:float = 0.0
bmi:float = 0.0
status:str = EMPTY
inches:float = 0.0
feets:float = 0.0
yards:float = 0.0

def to_celsius(temp: float, pretty: bool = True) -> float:
    '''
    Convert temperature from fahrenheit to celsius
    '''
    celsius = (temp - 32) * (5/9)
    return f"{celsius:.2f}" if pretty else celsius

def to_fahrenheit(temp: float, pretty: bool = True) -> float:
    '''
    Convert temperature from celsius to fahrenheit
    '''
    fahrenheit = temp*(9/5)+32
    return f"{fahrenheit:.2f}" if pretty else fahrenheit

def bmi(weight: float,height: float, pretty: bool = True) -> str:
    '''
    BMI = weight (kg) / [height (m)]2
    '''
    bmi = weight / (height ** 2)

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

    bmi = f"{bmi:.2f}" if pretty else bmi

    return f"BMI: {bmi}, status: {status}"


def to_inches(distance: float, pretty: bool = True) -> float:
    '''
    Convert distance from kilometers to inches
    '''
    inches = distance*INCHES
    return f"{inches:.2f}" if pretty else inches

def to_feets(distance: float, pretty: bool = True) ->  float:
    '''
    Convert distance from kilometers to feets
    '''
    feets = distance*FEETS
    return f"{feets:.2f}" if pretty else feets

def to_yards(distance: float, pretty: bool = True) ->  float:
    '''
    Convert distance from kilometers to yards
    '''
    yards = distance*YARDS
    return f"{yards:.2f}" if pretty else inches

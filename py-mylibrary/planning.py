'''
Planning Module
'''
import datetime as dt

# CONSTANTS DE L'ORDRE DE CADA MÉS A L'ANY
JANUARY = 1
FEBRUARY = 2
MARCH = 3
APRIL = 4
MAY = 5
JUNE = 6
JULY = 7
AUGUST = 8
SEPTEMBER = 9
OCTOBER = 10
NOVEMBER = 11
DECEMBER = 12

# CONSTANTS DELS DIES QUE TÉ UN ANY DE TRASPÀS (BISIESTO) I UN QUE NO HO ÉS
LEAPDAYS = 366
NOLEAPDAYS = 365

# FUNCIONS A NIVELL DE CLASS
def current_year() -> int:
    '''Return the current year'''
    today = dt.date.today()
    return today.year

    #return dt.datetime.now().year

def elapsed_days(varyear: int = current_year()) -> int:
    '''Return the elapsed days of the function input year'''
    today = dt.date.today()
    day = dt.date(year = varyear, month = today.month, day = today.day)
    # first_date = today.replace(month = JANUARY, day = 1)
    first_date = dt.date(year = day.year, month = JANUARY, day = 1)
    interval = day - first_date

    return interval.days + 1

    # year_day = today.timetuple().tm_yday
    # first_day = dt.date.min.day
    # last_day = dt.date.max.day
    
def remaining_days(varyear: int = current_year()) -> int:
    '''Return the remaining days of the function input year'''
    today = dt.date.today()
    day = dt.date(year = varyear, month = today.month, day = today.day)
    # last_date = today.replace(month = DECEMBER, day = 31)
    last_date = dt.date(year = day.year, month = DECEMBER, day = 31)
    interval = last_date - day

    return interval.days
    # year_day = dt.date.today().timetuple().tm_yday
    # last_day = dt.date.max.day

def is_leap_year(year: int = current_year()) -> bool:
    '''Return True for leap years, False for non-leap years.'''
    # Opció amb ternari i condicions lògiques
    return True if (year % 4 == 0) and ((year % 100 != 0) or ((year % 100 == 0) and (year % 400 == 0))) else False
    
    # Opció amb if else
    # if year % 4 == 0:
    #    if year % 100 == 0:
    #        if year % 400 == 0:
    #            return True
    #    else:
    #        return True
    # return False

def total_days(year: int = current_year()) -> int:
    '''Return the number of total days by year'''
    return LEAPDAYS if is_leap_year(year) else NOLEAPDAYS

def prev_leap_year(year: int = current_year()) -> int:
    '''Return the previous leap year of the specified year'''
    while is_leap_year(year) == False:
        year -= 1
    return year
    

def next_leap_year(year: int = current_year()) -> int:
    '''Return the next leap year of the specified year'''
    while is_leap_year(year) == False:
        year += 1
    return year


def year_progress(pretty: bool = True, year: int = current_year()) -> float|str:
    '''Get the current year progress in percentage'''
    progress = elapsed_days(year) / total_days(year)
    # return progress
    return f"{progress:.2%}" if pretty else progress * 100

    #raise NotImplementedError("Not yet implemented!!!")

# TIPUS DE DADES PROPIS (CLASSES)
class Event:
    pass

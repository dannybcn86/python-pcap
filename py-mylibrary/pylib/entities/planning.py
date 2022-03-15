'''
Planning Module
'''
import datetime as dt
from pylib.entities import geometry

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
    '''
    Class Event
    '''
    # ATRIBUTS O CAMPS A NIVELL DE CLASS (STATIC/SHARED)
    MIN_VALUE: 'dt.date' = dt.date.today()
    _counter: int = 0
    
    # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
    def __init__(self, id: str, name: int, date: 'dt.date', start_time: 'dt.datetime.time', end_time: 'dt.datetime.time', background_color: 'geometry.Color', public: bool, description: str):
        Event._counter += 1
        self.id = id
        self.name = name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.background_color = background_color
        self.public = public
        self.description = description

    def duration():
        '''Python DocString'''
        pass

    def is_after():
        '''Python DocString'''
        pass

    def is_before():
        '''Python DocString'''
        pass

    def overloads():
        '''Python DocString'''
        pass

    @property
    def id(self):
        '''Python DocString'''
        return self._id
    
    @id.setter
    def id(self, value: str) ->str:
        '''Python DocString'''
        if not isinstance(value, str):
            raise TypeError("The id must be of type string.")
        self._id = value
    
    @property
    def name(self):
        '''Python DocString'''
        return self._name
    
    @name.setter
    def name(self, value: str):
        '''Python DocString'''
        if not isinstance(value, str):
            raise TypeError("The name must be of type string.")
        self._name = value

    @property
    def date(self):
        '''Python DocString'''
        return self._date
    
    @date.setter
    def date(self, value: 'dt.date'):
        '''Python DocString'''
        if not isinstance(value, dt.date):
            raise TypeError("The name must be of type datetime.date")
        if not value >= Event.MIN_VALUE:
            raise ValueError("The date of the event must be greather then or equal to today.")
        self._date = value

    @property
    def start_time(self):
        '''Python DocString'''
        return self._date
    
    @start_time.setter
    def start_time(self, value: 'dt.datetime.time'):
        '''Python DocString'''
        if not isinstance(value, dt.datetime.time):
            raise TypeError("The name must be of type datetime.datetime.time")
        self._start_time = value

    @property
    def end_time(self):
        '''Python DocString'''
        return self._date
    
    @end_time.setter
    def end_time(self, value: 'dt.datetime.time'):
        '''Python DocString'''
        if not isinstance(value, dt.datetime.time):
            raise TypeError("The name must be of type datetime.datetime.time")
        if not value > Event.start_time:
            raise ValueError("End time must be greather than start time.")
        self._end_time = value

    @property
    def background_color(self):
        '''Python DocString'''
        return self._date
    
    @background_color.setter
    def background_color(self, value: 'geometry.Color'):
        '''Python DocString'''
        if not isinstance(value, geometry.Color):
            raise TypeError("The name must be of type geometry.Color")
        self._background_color = value

    @property
    def public(self):
        '''Python DocString'''
        return self._public
    
    @public.setter
    def public(self, value: bool):
        '''Python DocString'''
        if not isinstance(value, bool):
            raise TypeError("The public must be of type bool.")
        self._public = value
    
    @property
    def description(self):
        '''Python DocString'''
        return self._description
    
    @description.setter
    def description(self, value: str):
        '''Python DocString'''
        if not isinstance(value, str):
            raise TypeError("The description must be of type str.")
        self._description = value
    
    def __len__(self, value: 'Event') -> tuple[dt.datetime.hour|dt.datetime.minute]:
        '''Python DocScrint'''
        return duration(value)
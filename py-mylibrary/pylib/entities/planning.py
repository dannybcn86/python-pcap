'''
Planning Module
'''
import datetime as dt
from time import time
from pylib.entities import geometry
from pylib.utils import strutils

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

def to_dhm(value):
    '''Python DocString'''
    dia = dt.datetime.fromtimestamp(value).day
    hora = dt.datetime.fromtimestamp(value).hour
    minut = dt.datetime.fromtimestamp(value).minute
    return (dia,hora, minut)

# TIPUS DE DADES PROPIS (CLASSES)
class Event:
    '''
    Class Event
    '''
    # ATRIBUTS O CAMPS A NIVELL DE CLASS (STATIC/SHARED)
    MIN_DAY: 'dt.date' = dt.date.today()
    MIN_TIME = dt.time(hour=0, minute=0)
    MAX_TIME = dt.time(hour=23,minute=59)
    _counter: int = 0
    
    # INICIALITZADOR D'OBJECTE ("CONSTRUCTOR")
    def __init__(self, name: int, date: 'dt.date', id: str=strutils.randcode(), start_time: 'dt.datetime' = MIN_TIME, end_time: 'dt.datetime' = MAX_TIME, background_color: 'geometry.Color' = geometry.DEFAULT_BG_COLOR, public: bool = True, description: str = strutils.EMPTY):
        Event._counter += 1
        self.id = id
        self.name = name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.background_color = background_color
        self.public = public
        self.description = description

    
    def duration(self, date: 'dt.date.day', start_time: 'dt.datetime', end_time: 'dt.datetime') -> tuple[dt.datetime|dt.datetime]:
        '''Python DocString'''
        start_timestamp = dt.datetime.combine(date = date, time=start_time).timestamp()
        end_timestamp = dt.datetime.combine(date = date, time=end_time).timestamp()
        diff_timestamp = end_timestamp - start_timestamp
        (dia, hora, minut) = to_dhm(value=diff_timestamp)
        return (hora,minut)

    def time_left(self,date:dt.date, start_time:dt.time) -> 'tuple[dt.date|dt.time|dt.time]|str':
        '''Temps que queda per iniciar el event'''
        aratimestamp = dt.datetime.now().timestamp()
        datainicitimestamp = dt.datetime.combine(date = date, time=start_time).timestamp()
        
        if aratimestamp < datainicitimestamp:
            diff_timestamp = datainicitimestamp - aratimestamp
            (dia, hora, minut) =  to_dhm(value=diff_timestamp)
            return (dia, hora, minut)
        else:
            print("L'event està succeint o ja ha succeit")
            return False

    def time_passed(self,date:dt.date, end_time:dt.time) ->bool:
        '''Temps des de la data de finalització del event'''
        aratimestamp = dt.datetime.now().timestamp()
        datafitimestamp = dt.datetime.combine(date = date, time=end_time).timestamp()
        
        if aratimestamp > datafitimestamp:
            diff_timestamp = aratimestamp - datafitimestamp
            (dia, hora, minut) = to_dhm(diff_timestamp)
            return (dia, hora, minut)
        else:
            print("L'event està succeint o encara no ha succeit")
            return False

    def uncoming(self, date:dt.date, start_time:dt.time) ->bool:
        '''La funció retorna True si encara no ha començat'''
        ara = dt.datetime.now()
        datainici = dt.datetime.combine(date = date, time=start_time)
        
        return True if ara < datainici else False

    def inprogress(self, date:dt.date, start_time:dt.time, end_time:dt.time) -> bool:
        '''La funció retorna True si està succeint'''
        ara = dt.datetime.now()
        datainici = dt.datetime.combine(date = date, time=start_time)
        datafi = dt.datetime.combine(date = date, time=end_time)

        return True if datainici <= ara <= datafi else False

    def finished(self, date:dt.date, end_time:dt.time) -> bool:
        '''La funció retorna True si ha finalitzat'''
        ara = dt.datetime.now()
        datafi = dt.datetime.combine(date = date, time=end_time)

        return True if ara > datafi else False

    def is_before(self, other: 'Event') -> bool:
        '''La funció retorna True si el nou event és avans del primer'''
        True if self.start_time > other.end_time else False

    def is_after(self, other: 'Event') -> bool:
        '''La funció retorna True si el nou event és després del primer'''
        True if other.start_time > self.end_time else False

    def overloaps(self, other: 'Event') -> bool:
        '''La funció retorna True si el nou event coincideix amb el primer'''
        True if ( self.start_time <= other.start_time <= self.end_time ) or (other.start_time <= self.start_time <= other.end_time) else False

    @classmethod
    def sample(cls):
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
        if not value >= Event.MIN_DAY:
            raise ValueError("The date of the event must be greather than or equal to today.")
        self._date = value

    @property
    def start_time(self):
        '''Python DocString'''
        return self._date
    
    @start_time.setter
    def start_time(self, value: 'dt.datetime'):
        '''Python DocString'''
        if not isinstance(value, dt.datetime):
            raise TypeError("The name must be of type datetime.datetime")
        self._start_time = value

    @property
    def end_time(self):
        '''Python DocString'''
        return self._date
    
    @end_time.setter
    def end_time(self, value: 'dt.datetime'):
        '''Python DocString'''
        if not isinstance(value, dt.datetime):
            raise TypeError("The name must be of type datetime.datetime")
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
    
    def __str__(self) -> str:
        '''Python DocString'''
        return f"{self.name} > {dt.datetime.combine(date=self.date, time=self.start_time)}"
    
    def __repr__(self):
        '''Python DocString'''
        return f"Id: {self.id}, Event: {self.name}, Programació: {self.date} {self.start_time} to {self.end_time}, background_color: {self.background_color}, public: {self.public}, description: {self.description}"

    def __len__(self) -> tuple[dt.datetime.minute]:
        '''Python DocScrint'''
        return self.duration()
    
    def __sub__(self, other: 'Event') -> tuple[dt.datetime.day|dt.datetime.hour|dt.datetime.minute]:
        '''Funció de retorna dies, hores i minuts entre dos events'''
        if self.is_after(other):
            duration = self.duration(self.end_time,other.start_time)
        elif self.is_before(other):
            duration = self.duration(other.end_time,self.start_time)
        return duration

    def __lt__(self, other: 'Event') -> bool:
        '''Python DocString'''
        pass

    def __le__(self, other: 'Event') -> bool:
        '''Python DocString'''
        pass

    def __gt__(self, other: 'Event') -> bool:
        '''Python DocString'''
        pass

    def __ge__(self, other: 'Event') -> bool:
        '''Python DocString'''
        pass
    
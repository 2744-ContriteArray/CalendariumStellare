import datetime as dt

# TODO:
# [] Figure out library structure
#   - what goes into stardate obj and what needs to go elsewhere?
#   [] setup.py
# [] Nail down conversion formulae
# [] Nail down zero day
# [] implement zero day and formulae
# [] create format for stardates
# [] function to convert datetime.datetime to int elements
#   - use datetime.timedelta?
#   - https://docs.python.org/3/library/datetime.html
# [] function to convert gregorian (with time) to Julian
# [] function to convert greg to jules (sans clock)
# [] implement into calculator functions
#   [] enter date on greg calendar, get stardate out
#   [] enter stardate, test validity, and get greg date out


# Constants
daysInYear = 360
hoursInDay = 30
minutesInHour = 60
secInMin = 60
# zeroDayGreg = datetime()
# zeroDayJules = datetime()


class stardate:
    datum: float

    def __init__(self):
        # initialize the object
        self.datum = 0.0

    def getDate(self):
        return self.datum

    def setDate(self, when):
        self.datum = when

    def calcDate(self, Jules: dt.datetime):
        # take the parts of the date and calculate the stardate (INCLUDING HOURS/MINUTES/SECONDS)
        when = 0.0
        # calculate the star year
        year = 0

        when += year*1000

        # calculate star day
        day = 0

        when += day

        # calculate star hour
        hour = 0

        when += hour/100

        # calculate star minute
        minute = 0

        when += minute/10000


# Functions

# purpose: convert gregorian date (including time of day) to Julian Calendar
def gregToJulianFull(self, when: dt.datetime):
    # Basic conversion for dates between 1901 and 2099 is Gregorian date minus 13 days
    # the gap in days grows by 3 every 400 years (0.0075 days per year)
    j = 1
    return j


# purpose: convert gregorian date (NOT including time of day) to Julian Calendar
def gregToJulianPart(self, when: dt.date):
    # JC = GC - 13
    j = 1
    return j


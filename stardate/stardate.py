import datetime as dt
import math

# TODO:
# [] Figure out library structure
#   - what goes into stardate obj and what needs to go elsewhere?
#   [] setup.py
# [] Nail down conversion formulae
# [] Nail down zero day
# [] implement zero day and formulae
# [] create format for stardates
# [] Numeric base conversion functions
#   [*] Decimal to hex
#   [] hex to dec
# [] function to convert datetime.datetime to int elements
#   - use datetime.timedelta?
#   - https://docs.python.org/3/library/datetime.html
# [*] function to convert gregorian (with time) to Julian
# [*] function to convert greg to jules (sans clock)
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


# Functions

# purpose: convert gregorian date (including time of day) to Julian Calendar
def gregToJulianFull(when: dt.datetime):
    # Basic conversion for dates between 1901 and 2099 is Gregorian date minus 13 days
    # the gap in days grows by 3 every 400 years (0.0075 days per year)
    j = when - dt.timedelta(days=13.0075)
    return j


# purpose: convert gregorian date (NOT including time of day) to Julian Calendar
def gregToJulianPart(when: dt.date):
    # JC = GC - 13
    j = when - dt.timedelta(days=13.0075)
    return j

def julToGreg(when:dt.datetime):
    g = when + dt.timedelta(days=13.0075)
    return g

def julToGregAbr(when:dt.date):
    return when + dt.timedelta(days=13.0075)

class stardate:
    datum = []*6

    def __init__(self):
        # initialize the object
        self.datum[3] = '.'

    def getDate(self):
        return self.datum

    def setDate(self, when: list):
        for i in when:
            if i == '.':
                continue
            else:
                    self.datum[i] = when[i]

    def decToHex(self, dec: int):
        hex = ""
        buff = []
        numLett = ['A', 'B', 'C', 'D', 'E', 'F']

        # do the math
        while dec > 0:
            # if the remainder > 9, it's a letter not 10-16
            if (dec%16) >= 10 and not((dec%16) > 15):
                buff.append(numLett[(dec%16)-10])
            else:
                # remainder is not >9
                buff.append(dec%16)

            # amend dec to reflect dec/16 without the remainder as floats
            dec = math.floor(dec/16)

        # assemble the remainders into the hex number
        for i in range(5, 0, -1):
            hex += buff[i]

        return hex

    def hexToDec(self, hex):
        dec = 0

        return dec

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



import datetime
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

# zero day in Julian Calendar
zeroDayJules = datetime.datetime(1970, 7, 31, 0, 0, 0)


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

## CONVERSION METHODS
# Run formulae for converting from Julian Calendar
#    def __ConvYear(self, Jules: dt.datetime):
#        year = " "

#        return year

#    def __ConvDay(self, Jules: dt.datetime):
#        day = " "

#        return day

#    def __ConvHour(self, Jules: dt.datetime):
#        hour = " "

#        return hour

## CALCULATION METHODS
# Run formulae for calculating independent of other calendars

    ## def __CalcYear(self):
    #     year = " "
    #
    #     return year
    #
    # def __CalcDay(self):
    #     day = " "
    #
    #     return day
    #
    # def __CalcHour(self):
    #     hour = " "
    #
    #     return hour


    # Set the object's year to the converted Stellar Year
    def setYear(self, when: str):
        self.datum[0] = when

    # Set the object's year to the unconverted Gregorian year
    def conv_setYear(self, when: dt.datetime):
        JC = gregToJulianFull(when)
        self.datum[0] = self.calcDateJ(JC)[0]

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

    def calcDateG(self, Greg: dt.datetime):
        when1 = gregToJulianFull(Greg)

        when2 = self.calcDateJ(self, when1)
        return when2

# NOT including hours/minutes
    def calcDateGpart(self, Greg: dt.date):
        when1 = gregToJulianPart(Greg)

        when2 = self.calcDateJ(when1)

        return when2

    def calcDateJ(self, Jules: dt.datetime):
        # take the parts of the date and calculate the stardate (INCLUDING HOURS/MINUTES/SECONDS)
        when = []*6

        # calculate the days since zero. this operation
        # returns a dt.timedelta obj that contains the
        # difference in days, hours, minutes, etc
        delta = Jules - zeroDayJules
        # calculate the hours since zero
        Y = Jules.year - zeroDayJules.year

        H = (delta.days*24)

        # calculate the stellar year and convert to hex
        StellarYear = math.floor((H/30 - Y*0.25)/360)
        when[0] = self.decToHex(StellarYear)

        # convert days (floor it to keep it whole)
        # TODO
        # [] refine formula for days
        #   - how do we whittle the days elapsed down
        #     to just the incomplete year?
        #   - math.floor(H/60 - H/30)%360

        # calculate days and then take the remainder of dividing that by 360
        StellarDay = math.floor(H/30 - Y*0.25)%360
        when[1] = self.decToHex(StellarDay)

        # convert hours
        # Timedelta objects return seconds, not minutes, and our formula requires
        # minutes. take those seconds since 0day and
        # divide by 60 in order to yield minutes
        M = math.floor(delta.seconds/60)

        # D (Julian days elapsed) = floor(Julian hours elapsed/30)
        # Y (Julian years elapsed) = floor(D/360)
        # M (Julian minutes elapsed) = floor(Seconds/60)
        # H (Julian hours elapsed) = floor(M/60) divided by 60 to yield the elapsed hours
        # Can also be found via H = timedelta.days*24
        # SH = H mod 30 to take the remainder of completed days
        StellarHour = H%30
        when[2] = str(StellarHour)

        # Calculate stellar minutes

        # when[4] =

        # Calculate stellar seconds

        # when[5] =

        return when

    def calcDateJpart(self, Jules: dt.date):
        # take parts of the date and calculate the stardate (EXCLUDING HOURS/MINUTES)
        when = [" "]*6

        return when

    #def calcDateInd(self):
import datetime as dt
import math

# TODO:
# [] Figure out library structure
#   - what goes into stardate obj and what needs to go elsewhere?
#   [*] setup.py
#       [*] create
#       [*] populate
#   [*] PyPi workflow configurement
# [] Nail down conversion formulae
#   [] Conversion method(s) from Jul/Greg -> Stardate
#   [] Conversion method(s) from Stardate -> Jul/Greg
#   [] calcDateJ()
#       [] calculate minutes
#       [] calculate seconds
# [] Verification methods
#   [] Is stardate equivalent to greg/jule year?
#       - how take parameters? take any at all? what use cases?
#       - called when self.datum or self.Gregorian are changed to keep them consistent
#       - if returns false (meaning their not equivalent) update the old to match the new
#   [] validity of stardate
#       - date info passed through __int__ and setters, need to verify that supplied info follows format
#       - called in setter methods
#       - if returns false, add handling to setters
# [] Handling in __init__ for non-default values
#   [*] add parameter for stardate info
#   [] verify congruency, handle incongruence
#   [] if one is default and other not, calculate and replace default
# [] set up documentation string stubs
# [] Documentation
#   - in README or in separate file(s)?


# Constants
# daysInYear = 360
# hoursInDay = 30
# minutesInHour = 60
# secInMin = 60
zeroDayGreg = dt.datetime(1970, 8, 13, 0, 0, 0)

# zero day in Julian Calendar
zeroDayJules = dt.datetime(1970, 7, 31, 0, 0, 0)
zeroDayJinc = dt.date(1970, 7, 31)


# Functions

# purpose: convert Gregorian date (including time of day) to Julian Calendar
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


## CONVERSION METHODS
# Run formulae for converting to Julian Calendar
def Conv2Jules_Part(when: stardate):
    year = 0
    month = 0
    day = 0

    return dt.date(year,month,day)

def Conv2Jules(when: stardate):
    year = 0
    month = 0
    day = 0
    hour = 0
    minute = 0

    return dt.datetime(year,month, day, hour, minute)

class stardate:
    __datum = [''] * 6
    __Gregorian: dt.datetime

    def __init__(self, when=dt.datetime(1970,1,1,0,0,0), Stellar=["00"]*6):
        # initialize the object
        self.__datum[3] = '.'
        self.__Gregorian = when
        if Stellar is not None:
            for i in range(len(self.__datum)):
                if self.__datum[i] == ".":
                    continue
                else:
                    self.__datum[i] = Stellar[i]

        # Convert when to Julian and then to stardate
        converted = self.calcDateG(when)

        # assign self.datum
        self.setStardate(converted)

    def getStardate(self):
        return self.__datum

    def setStardate(self, when: list):
        for i in when:
            if i == '.':
                continue
            else:
                    self.__datum.append(i)# = when[i]



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
    def setStarYear(self, when: str):
        self.__datum[0] = when

    def getStarYear(self):
        return self.__datum[0]

    # Set the object's year to the unconverted Gregorian year
    def conv_setYear(self, when: dt.datetime):
        JC = gregToJulianFull(when)
        self.__datum[0] = self.calcDateJ(JC)[0]

    def decToHex(self, dec: int):
        hexa = ""
        buff = ['']
        numLett = ['A', 'B', 'C', 'D', 'E', 'F']

        # do the math
        #iter = 0
        while dec > 0:
            # if the remainder > 9, it's a letter not 10-16
            if (dec%16) >= 10 and not((dec%16) > 15):
                #buff[iter] = numLett[(dec%16)-10]
                buff.append(numLett[(dec%16)-10])
            else:
                # remainder is not >9
                #buff[iter] = dec%16
                buff.append(str(dec%16))

            # amend dec to reflect dec/16 without the remainder as floats
            dec = math.floor(dec/16)

            #iter += 1

        # assemble the remainders into the hex number
        # THROWS LIST INDEX OUT OF RANGE ERROR
        #print("in decToHex\n len(buff[]) = ", len(buff))
        for i in range(len(buff)-1, 0, -1):
            hexa += str(buff[i])

        return hexa

    @staticmethod
    def hexToDec(hexaD: str):
        # PROCESS
        # Multiply each digit of hex number by 16, raised to the power of its position
        #   starting from 0
        # Add up the results of these multiplications
        # ex. A.4 = (A*16^0) + (4*16^-1) = (10*1) + (4*0.0625) = 10.25
        dec = 0
        # For to convert the letter digits into decimal ints
        Letters = {"A": 10, "a": 10, "B": 11, "b": 11, "C": 12, "c": 12,
                   "D": 13, "d": 13, "E": 14, "e": 14, "F": 15, "f": 15}

        # convert hex
        power = len(hexaD)
        for i in hexaD:
            digit = 0

            #handle decimals - unlikely to be necessary but always good to account for
            if i == ".":
                power = -1
                continue

        # handle the letters and cast from str to int
            if i in Letters:
                digit = Letters[i]
            else:
                digit = int(i)

            # convert digit to decimal and add to the final integer
            dec += digit*(pow(16,power))

            power -= 1


        return dec

    def calcDateG(self, Greg: dt.datetime):
        when1 = gregToJulianFull(Greg)

        when2 = self.calcDateJ(when1)
        return when2

# NOT including hours/minutes
    def calcDateGpart(self, Greg: dt.date):
        when1 = gregToJulianPart(Greg)

        when2 = self.calcDateJpart(when1)

        return when2

    def calcDateJ(self, Jules: dt.datetime):
        # take the parts of the date and calculate the stardate (INCLUDING HOURS/MINUTES/SECONDS)
        when = ['']*6

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
        when[1] = str(StellarDay)

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
        when[3] = "."

        # Calculate stellar minutes

        # when[4] =

        # Calculate stellar seconds

        # when[5] =

        when[4] = "00"
        when[5] = "00"

        return when

    def calcDateJpart(self, Jules: dt.date):
        # take parts of the date and calculate the stardate (EXCLUDING HOURS/MINUTES)
        when = [" "]*6
        when[3] = "."
        when[2] = "00"
        when[4] = "00"
        when[5] = "00"

        # calculate the days since zero. this operation
        # returns a dt.timedelta obj that contains the
        # difference in days, hours, minutes, etc
        delta = Jules - zeroDayJinc
        # calculate the hours since zero
        Y = Jules.year - zeroDayJinc.year

        H = delta.days*24

        # calculate the stellar year and convert to hex
        StellarYear = math.floor((H/30 - Y*0.25)/360)
        when[0] = self.decToHex(StellarYear)


        # calculate days and then take the remainder of dividing that by 360
        StellarDay = math.floor(H/30 - Y*0.25)%360
        when[1] = str(StellarDay)

        return when

    #def calcDateInd(self):

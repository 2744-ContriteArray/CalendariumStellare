import datetime as dt
import math

# TODO:
#  [] Figure out library structure
#   - what goes into stardate obj and what needs to go elsewhere?
#   [*] setup.py
#       [*] create
#       [*] populate
#   [*] PyPi workflow configurement
#   [] Nail down conversion formulae
#   [] Conversion method(s) from Jul/Greg -> Stardate
#   [] Conversion method(s) from Stardate -> Jul/Greg
#   [] calcDateJ()
#       [] calculate minutes
#       [] calculate seconds
#       [] Verification methods
#   [] Is stardate equivalent to greg/jule year?
#       - how take parameters? take any at all? what use cases?
#       - called when self.datum or self.Gregorian are changed to keep them consistent
#       - if returns false (meaning their not equivalent) update the old to match the new
#   [] validity of stardate
#       - date info passed through __int__ and setters, need to verify that supplied info follows format
#       - called in setter methods
#       - if returns false, add handling to setters
#       [] Handling in __init__ for non-default values
#           [] when
#           [*] Stellar
#       [*] add parameter for stardate info
#       [] verify congruency, handle incongruence
#       [] if one is default and other not, calculate and replace default
#   [] Documentation
#       [] set up documentation string stubs
#      - in README or in separate file(s)?


# Constants
# daysInYear = 360
# hoursInDay = 30
# minutesInHour = 60
# secInMin = 60
zeroDayGreg = dt.datetime(1970, 8, 13, 0, 0, 0)

# zero day in Julian Calendar
zeroDayJules = dt.datetime(1970, 7, 31, 0, 0, 0)
zeroDayJ_inc = dt.date(1970, 7, 31)

class stardate:
    __datum = [''] * 6
    __Gregorian: dt.datetime

    def __init__(self, when=dt.datetime(1970,1,1,0,0,0), Stellar=[""]*6):
        """

        :type Stellar: List[""]
        :type when: datetime.datetime
        """
        # initialize the object
        if Stellar is None:
            Stellar = ["00"] * 6
        self.__datum[3] = '.'
        self.__Gregorian = when
        if Stellar is not None:
            for i in range(len(self.__datum)-1):
                if self.__datum[i] == ".":
                    continue
                else:
                    self.__datum[i] = Stellar[i]
        else:
            for i in range(len(self.__datum)-1):
                self.__datum[i] = "00"
            self.__datum[3] = "."

        # Convert when to Julian and then to stardate
        converted = self.calcDateG(when)

        # assign self.datum
        self.setStardate(converted)

    # Static Functions

    # purpose: convert Gregorian date (including time of day) to Julian Calendar
    @staticmethod
    def gregToJulianFull(when: dt.datetime):
        """

        :type when: dt.datetime
        """
        # Basic conversion for dates between 1901 and 2099 is Gregorian date minus 13 days
        # the gap in days grows by 3 every 400 years (0.0075 days per year)
        j = when - dt.timedelta(days=13.0075)
        return j

    # purpose: convert Gregorian date (NOT including time of day) to Julian Calendar
    @staticmethod
    def gregToJulianPart(when: dt.date):
        """
        :param when: dt.date
        :return: dt.date
        """
        # JC = GC - 13
        j = when - dt.timedelta(days=13.0075)
        return j

    @staticmethod
    def julToGreg(when: dt.datetime):
        g = when + dt.timedelta(days=13.0075)
        return g

    @staticmethod
    def julToGregAbr(when: dt.date):
        return when + dt.timedelta(days=13.0075)

## CONVERSION FROM STARDATE TO JULIAN
    # Run formulae for converting to Julian Calendar
    @staticmethod
    def Conv2Jules_Part(when: stardate):
        year = 0
        month = 0
        day = 0

        return dt.date(year, month, day)

    # Convert stardate to Julian calendar
    @staticmethod
    def Conv2Jules(when: stardate):
        year = 0
        month = 0
        day = 0
        hour = 0
        minute = 0

        return dt.datetime(year, month, day, hour, minute)

    def getStardate(self):
        return self.__datum

    def setStardate(self, when: list):
        for i in when:
            if i == '.':
                continue
            else:
                    self.__datum.append(i)# = when[i]

    # Set the object's year to the converted Stellar Year
    def setStarYear(self, when: str):
        self.__datum[0] = when

    def getStarYear(self):
        return self.__datum[0]

    # Set the object's year to the unconverted Gregorian year
    # TODO
    #  [] Verify that date lines up with obj current stardate
    #  [] Update stardate if not
    def conv_setYear(self, when: dt.datetime):
        JC = self.gregToJulianFull(when)
        self.__datum[0] = self.calcDateJ(JC)[0]

    # Should this method be static? Private?
    def decToHex(self, dec: int):
        hexa = ""
        buff = ['']
        numLett = ['A', 'B', 'C', 'D', 'E', 'F']

        # do the math
        while dec > 0:
            # if the remainder > 9, it's a letter not 10-16
            if (dec%16) >= 10 and not((dec%16) > 15):
                buff.append(numLett[(dec%16)-10])
            else:
                # remainder is not >9
                buff.append(str(dec%16))

            # amend dec to reflect dec/16 without the remainder as floats
            dec = math.floor(dec/16)

        # assemble the remainders into the hex number
        for i in range(len(buff)-1, 0, -1):
            hexa += str(buff[i])

        return hexa

    # Should this method be static? Private?
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
            digit: int

            #handle decimals - unlikely to be necessary but always good to account for
            if i == ".":
                power = -1
                continue

        # handle the letters and cast from str to int
            if i in Letters.keys():
                digit = Letters[i]
            else:
                digit = int(i)

            # Error mitigation
            if digit is None:
                digit = 0

            # convert digit to decimal and add to the final integer
            dec += digit*(pow(16,power))

            power -= 1


        return dec

    # Calculate stardate from Gregorian
    def calcDateG(self, Greg: dt.datetime):
        when1 = self.gregToJulianFull(Greg)

        when2 = self.calcDateJ(when1)
        return when2

    # NOT including hours/minutes
    def calcDateG_part(self, Greg: dt.date):
        when1 = self.gregToJulianPart(Greg)

        when2 = self.calcDateJpart(when1)

        return when2

    #TODO
    # [] Implement formula for calculating stellar minutes
    # [] Implement formula for calculating stellar seconds
    def calcDateJ(self, Jules: dt.datetime):
        # take the parts of the date and calculate the stardate (INCLUDING HOURS/MINUTES/SECONDS)
        when = ['']*6

        # calculate the days since zero. this operation
        # returns a dt.timedelta obj that contains the
        # difference in days, hours, minutes, etc
        delta = Jules - zeroDayJules
        # calculate the hours since zero
        Y = Jules.year - zeroDayJules.year

        H = math.floor((delta.days*24) + (delta.seconds/60)/60)

        # calculate the stellar year and convert to hex
        StellarYear = math.floor((H/30 - Y*0.25)/360)
        when[0] = self.decToHex(StellarYear)

        # convert days (floor it to keep it whole)
        # calculate days and then take the remainder of dividing that by 360
        StellarDay = math.floor(H/30 - Y*0.25)%360
        when[1] = str(StellarDay)

        # convert hours
        # Timedelta objects return seconds, not minutes, and our formula requires
        # minutes. take those seconds since 0day and
        # divide by 60 in order to yield minutes
        print("In calcDateJ()")
        M = math.floor((delta.seconds/60)%60)
        print("M = ", M)
        S = delta.seconds%60
        print("S = ", S)

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
            # OPTION 1
                # Take Y and perform f(Y)=floor(Y*365 - Y*0.25)*24 to yield the total hours
                    # H += f(Y)
                # Take H and multiply by 60 to turn it into minutes
                # Subtract that from M to get the adjusted remaining minutes
            # OPTION 2
                # M = math.floor(delta.seconds/60)
                # H2 = M/60
            # OPTION 3
                # SM = M
                # SS = S

        # when[4] =

        # Calculate stellar seconds

        # when[5] =
        if M < 10:
            when[4] = "0"+str(M)
        else:
            when[4] = str(M)#"00"

        if S < 10:
            when[5] = "0"+str(S)
        else:
            when[5] = str(S)#"00"

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
        delta = Jules - zeroDayJ_inc
        # calculate the hours since zero
        Y = Jules.year - zeroDayJ_inc.year

        H = delta.days*24

        # calculate the stellar year and convert to hex
        StellarYear = math.floor((H/30 - Y*0.25)/360)
        when[0] = self.decToHex(StellarYear)


        # calculate days and then take the remainder of dividing that by 360
        StellarDay = math.floor(H/30 - Y*0.25)%360
        when[1] = str(StellarDay)

        return when

    #def calcDateInd(self):

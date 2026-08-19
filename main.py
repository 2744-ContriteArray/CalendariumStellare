import datetime

# TODO:
# [] Decide on zero date
# [] function to convert datetime.datetime to int elements
#   - use datetime.timedelta?
#   - https://docs.python.org/3/library/datetime.html
# [] function to convert gregorian (with time) to Julian
# [] function to convert greg to jules (sans clock)
# [] nail down conversion formulae for stardates
# [] implement into calculator function
#   - enter date on greg calendar, get stardate out
# [] implement function to convert rightNow into present stardate
#   - threaded and continuously running
# [] GUI

# Constants
daysInYear = 360
hoursInDay = 30
# zeroDayGreg = datetime()
# zeroDayJules = datetime()
rightNow = datetime.datetime.now()

def gregToJulianFull(when: datetime.datetime):
    # Basic conversion for dates between 1901 and 2099 is Gregorian date minus 13 days
    # the gap in days grows by 3 every 400 years (0.0075 days per year)
    j = 1

def gregToJulianPart(when: datetime.date):
    # JC = GC - 13
    j = 1

def main():
    print("Dia duit, a dhomhain!")

main()
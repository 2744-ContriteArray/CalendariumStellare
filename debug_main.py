import datetime as dt
import stardate.stardate
#import tkinter as tk

# TODO:
# [*] stardate library/module setup
# [*] Class for stardate objects
# [] complete stardate.py and build library
# [] implement function to convert rightNow into present stardate
#   - threaded and continuously running
# [] GUI


rightNow = dt.datetime.now()
rightNowAbbr = dt.date(rightNow.year,rightNow.month,rightNow.day)

# Purpose: convert rightNow to Julian calendar and then use timedelta to calculate stardate
def rnStardate():
    nowJules = rightNow #placeholder
    return nowJules

def main():
    print("Dia duit, a dhomhain!")
    calculator = stardate.stardate.stardate(rightNow)
    starNow = calculator.calcDateG(rightNow)
#    starNow = calculator.calcDateGpart(rightNowAbbr)
    starString = ""

    for i in starNow:
        starString += i

    print("CURRENT STARDATE IS:")
    print(starString)

main()
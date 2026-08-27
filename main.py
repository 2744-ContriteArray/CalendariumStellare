import datetime as dt
#import stardate as sd
import tkinter as tk

# TODO:
# [*] stardate library/module setup
# [*] Class for stardate objects
# [] complete stardate.py and build library
# [] implement function to convert rightNow into present stardate
#   - threaded and continuously running
# [] GUI


rightNow = dt.datetime.now()

# Purpose: convert rightNow to Julian calendar and then use timedelta to calculate stardate
def rnStardate():
    nowJules = rightNow #placeholder
    return nowJules

def main():
    print("Dia duit, a dhomhain!")

main()
import datetime
import stardate

# TODO:
# [*] stardate library/module setup
# [*] Class for stardate objects
# [] implement function to convert rightNow into present stardate
#   - threaded and continuously running
# [] GUI


rightNow = datetime.datetime.now()

# Purpose: convert rightNow to Julian calendar and then use timedelta to calculate stardate
def rnStardate():
    nowJules = rightNow #placeholder
    return nowJules

def main():
    print("Dia duit, a dhomhain!")

main()
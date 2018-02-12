# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    # True for leap year
    # False for common year

    if year % 4:
        return False
    elif year % 100:
        return True
    elif year % 400:
        return False
    else:
        return True


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    leap = 0 # counting leap years

    for i in range(y1, y2):

        if not isLeapYear(i):
            leap += 0
        else:
            leap += 1
    day = d2 - d1 # counting days
    if day < 0:
        if m2 == 1:
            m2 = m2 + 11
        day = day + daysOfMonths[m2]

    month = m2 - m1

    if month < 0:
        month = month + 12

    year = y2 - y1
    if year < 0:
        year = 0

    if m1 > m2:
        year -= 1



    days = int(leap + (year)* 365.25 + day + (month * 30.2))

    return days


print daysBetweenDates(2018, 10, 29, 2018, 11, 30)

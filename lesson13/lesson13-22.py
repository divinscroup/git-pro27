###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###


def nextDay(year, month, day):
    if day == 30:
        day -= 29
        month += 1
    else:
        day += 1
    if month -1 == 12: # using -1 in if statement that check the real value of month
        month = 1
        year += 1

    return year,month,day


print nextDay(2012,1,1)
print nextDay(2012, 4, 30)
print nextDay(2012, 12, 1)
print nextDay(1999, 12, 30)
print nextDay(2012, 6, 29) 
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a, b):
    if a > b:
        return a
    else:
        return b


def small(a, b):
    if a < b:
        return a
    return b


def median(a, b, c):
    if a > b:
        return small(a, (bigger(b, c)))
    return bigger(a, small(b, c))


print median(1, 2, 3)
# >>> 2

print median(9, 3, 6)
# >>> 6

print median(7, 8, 7)
# >>> 7








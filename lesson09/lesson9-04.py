# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.



def bigger(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a


print bigger(2, 7)
# >>> 7

print bigger(3, 2)
# >>> 3

print bigger(3, 3)
# >>> 3

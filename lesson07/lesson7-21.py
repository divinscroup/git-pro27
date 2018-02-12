# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.



def abbaize(a,b):
    return str(a)+str(b)+str(b)+str(a) # in case the inputs was numbers



print abbaize('a','b')

#print abbaize('a','b')
#>>> 'abba'

print abbaize('dog','cat')
#>>> 'dogcatcatdog'
# Once again, say_hello is a function (AKA procedure). But this time, it DOESN'T
# do the same thing every time.
#
# Read through the code and try to predict what the output will be when
# you press "Test Run"

def say_hello(name):
    greeting = "Hello " + name + "!"
    return greeting

print say_hello("Miriam")
print say_hello("Andy")

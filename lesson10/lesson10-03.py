# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

def bracket(text):
    return '[' + text + ']'

def boldwrap(text):
    return '<b>' + text + '</b>'

print boldwrap('This is an important message.')

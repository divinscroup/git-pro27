# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.
# Review Dave's video on string.find, or visit
# http://www.tutorialspoint.com/python/string_find.htm for more information.

text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""

noun_position = text.find('NOUN')  #fill this in
verb_position = text.find('VERB') #fill this in
print 'noun_position is : ' + str(noun_position) + '\n'
print 'verb_position is : ' + str(verb_position)

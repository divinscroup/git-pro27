import clipboard
import random

string = 'abcdefghigklmnopqrstuvwxyz'
Cstring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sym ='!@$.#'
val = f'{random.choice(string.upper())}{random.choice(string.lower())}{random.choice(sym)}20172017'
print(val)
clipboard.copy(val)




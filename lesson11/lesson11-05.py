# Write code for the function random_noun, which takes in no inputs but outputs
# one of two nouns randomly. Use the randint function to generate a number
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1.
# Feel free to experiment with different nouns, but for submission purposes return
# the string "sofa" if the number is 0, else return "llama".

from random import randint


def random_noun():
    x = randint(0, 1)
    if x == 0:
        return 'sofa'
    return 'llama'
    # your code here


print random_noun()

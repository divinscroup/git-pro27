# Let's put it all together. Write code for the function process_madlib, which takes in
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

from random import randint


def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"


def random_noun():
    random_num = randint(0, 1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"


def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word  # word[0] will destroy my solution ;(


def process_madlib2(mad_lib):
    i, processed, word = 0, "", 'NOUN'

    while i > -1:

        x = mad_lib.find(word, i)

        if x == -1:
            processed += mad_lib
        else:
            processed += mad_lib[:x]
        mad_lib = word_transformer(word) + mad_lib[x + 4:]
        i = x / 10

    mad_lib = processed

    i, processed, word = 0, '', 'VERB'

    while i > -1:

        x = mad_lib.find('VERB', i)

        if x == -1:
            processed += mad_lib
        else:
            processed += mad_lib[:x]
        mad_lib = word_transformer(word) + mad_lib[x + 4:]
        i = x / 10  # garantees that i not going out of range while find starting again

    mad_lib = processed

    return mad_lib


test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib2(test_string_1)
print process_madlib2(test_string_2)


##### another solution #######


def process_madlib(mad_lib):
    index, processed = 0, ''
    splt = mad_lib.split(' ')
    while index < splt.__len__():
        if len(splt[index]) == 4:
            splt[index] = word_transformer(splt[index])
        processed += splt[index] + ' '
        index += 1

    return processed


print process_madlib(test_string_1)
print process_madlib(test_string_2)


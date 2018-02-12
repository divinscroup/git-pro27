# This code demonstrates a while loop with a "counting variable"
i = 0
while i < 10:
    print i
    i = i + 1


# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
def remove_spaces(text):
    text_without_spaces = ''  # empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':  # that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces


print remove_spaces("hello my name is andy how are you?")


# another solution
def remove_spaces2(txt):
    i = 0
    d = ''
    while i < len(txt):
        if txt[i] != ' ':
            d = d + txt[i]
        txt = txt[1:]
    return d


print remove_spaces2("hello my name is andy how are you?")

# Set noun_replacement and verb_replacement to your own noun and verb strings.
# Then, concatenate the variables substring1-3, noun_replacement, and
# verb_replacement and assign the result to the variable new_sentence so that
# it's in the same order as the variable sentence.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "DUCK" # your noun here
verb_replacement = "RUN" # your verb here

new_sentence = ""
# your code here
new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3
print new_sentence

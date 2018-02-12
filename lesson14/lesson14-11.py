# Let's play around with one more string method: string.split(), which
# splits a string into a list of substrings, and returns it as a new list.
# Assign list_of_words1 to the split string1 and list_of_words2 to the split string2.

string1 = "Yesterday, PERSON and I went to the PLACE. On our way, we saw a ADJECTIVE NOUN on a bike."
string2 = "PLACE is located on the ADVERB side of Dublin, near the mainly ADJECTIVE areas of PLACE."
list_of_words1 = string1.split(' ')
list_of_words2 = string2.split(' ')

print list_of_words1
print list_of_words2

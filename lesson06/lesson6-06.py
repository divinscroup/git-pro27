# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB"
# in substring3.

sentence = "A NOUN went on a walk. It can VERB really fast."
# solution 1

substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]
print 'substring1 is : ' + substring1 + '\n'
print 'substring2 is : ' + substring2 + '\n'
print 'substring3 is : ' + substring3 + '\n'

# solution 2

sub1 = sentence[:sentence.find('NOUN')]
print 'substring1 is : ' + sub1 + '\n'
sub2_f = sentence.find(' went')
sub2_l = sentence.find('VERB')
print 'substring2 is : ' + sentence[sub2_f:sub2_l] + '\n'
sub3 = sentence[sentence.find(" re"):]
print 'substring3 is : ' + sub3 + '\n'


from random import randint

# with open(r'test.txt','w') as w:
#     w.write('hey this is amazing  teaching!')
#
# with open(r'test.txt','a') as w:
#     w.write('\nyes it is !')

ninja_words = [
    'aki', 'buyu', 'chimonjutsu', 'cho sen', 'dojo', 'gakusi',
    'haiboku', 'jin', 'kenshi', 'obaka ken', 'rakusha', 'sanmaru',
    'tekkon', 'yoko', 'zen'

]

def ninjarize():
    rand = randint(0,len(ninja_words)-1)
    return f'{ninja_words[rand]}'
para = int(input('how many paragraphs you want to generate :'))
count = int(input('how many word in paragraph: '))
lists = []
with open(r'test.txt','a') as f:

    for p in range(para):
        for c in range(count):
            if len(lists) % 10 == 0:
                lists.append('\n')
            lists.append(ninjarize())
            lists[1] = f'{lists[1].capitalize()}'

        f.write(' '.join(lists)+ '.\n')
        lists.clear()
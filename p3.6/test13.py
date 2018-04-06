def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')


def belt_count(dic):
    belts = list(dic.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'there are {num} {belt} belts!')


ninja_belts = {}
while True:
    ninja_name = input('Enter ninja name: ')
    ninja_belt = input('Enter a belt colour: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another ?(y/n)')
    if another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)
belt_count(ninja_belts)

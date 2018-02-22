print('Imported my module...')
test = 'Test any String'


def find_index(search, target):
    for i, value in enumerate(search):
        if value == target:
            return i
    return -1

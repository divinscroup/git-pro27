grades = ['A', 'B', 'C', 'F', 'A', 'F', 'B']
nums = [1, 2, 3, 4, 5]


def remove_fails(g):
    return g != 'F'


print(list(filter(remove_fails, grades)))
filters = []
for g in grades:
    if g != 'F':
        filters.append(g)
print(filters)

print([grade for grade in grades if grade != 'F'])

print(list(map(lambda n: n * n, nums)))

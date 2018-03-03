nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist = [n for n in nums]
print(mylist)
mylist = [n * n for n in nums]
print(mylist)
mylist = map(lambda n: n * n, nums)
print(*mylist)
mylist = [n for n in nums if n % 2 == 0]
print(mylist)
mylist = []
for l in 'abcd':
    for i in range(4):
        mylist.append([l, i])

print(mylist)
mylist = [[l, n] for l in 'abcd' for n in range(4)]
print(mylist)

names = ['bruce', 'clark', 'peter', 'logan', 'wade']
heros = ['batman', 'superman', 'spiderman', 'wolverene', 'deadpool']
mydict = {}
for name, hero in zip(names, heros):
    mydict[name] = hero
print(mydict)
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'peter'}
print(my_dict)

li = [-6, -5, -4, 1, 2, 3]
li_s = sorted(li, key=abs)
print(li_s)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '{} {} , ${}'.format(self.name, self.age, self.salary)


e1 = Employee('john', 34, 3000)
e2 = Employee('tom', 45, 4000)
e3 = Employee('jack', 44, 2500)
emp = [e1, e2, e3]


def e_sort(emp):
    return emp.salary


print(sorted(emp, key=e_sort, reverse=True))
print(sorted(emp, key=lambda e: e.name))

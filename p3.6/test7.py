import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('jack', '33')
sentnce = 'my name is {} and I am {} years old'.format(p1.name, p1.age)
print(sentnce)
person = {'name': 'jack', 'age': 33}
sentnce = 'my name is {name} and I am {age} years old'.format(**person)
print(sentnce)
for i in range(11):
    s = 'the value is {:02}'.format(i)
    print(s)

myDate = datetime.datetime(2016, 9, 24, 12, 30, 45)
sent = '{0:%B %d, %y} fell on a {0:%A} and was  the {0:%j} day of the year'.format(myDate)
print(sent)


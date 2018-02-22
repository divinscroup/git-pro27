def hi_func(greeting, name='you'):
    return '{} {}'.format(greeting, name)


print(hi_func('hi', 'oss'))


def stu(*args, **kwargs):
    print(args)
    print(kwargs)


course = ['math', 'physics', 'art']
info = {'name': 'john', 'age': 25, 'major': 'student'}

stu(*course, **info)

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return months[month]

print(days_in_month(2017, 2))



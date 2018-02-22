

x = lambda a1, a2: a1 + a2
print(x(1, 2))

h = 'hello'
w = 'world'
print(f'greetings and {h} {w.upper()}')
# print(help(str))
courses = ['math', 'history', 'physics', 'compsci']
# popped  = courses.pop()
# print(courses)
# print(popped)
for index, item in enumerate(courses, start=1):
    print(index,item)

courses_str = ' - '.join(courses)
print(courses_str)

student = {'name': 'john', 'age': 25, 'course': ['Math', 'CompSci']}
student.update({'name': 'jane', 'age': 27, 'phone': '555-4454'})
print(student)
for key,value in student.items():
    print(key, value)
# print(student['course'])
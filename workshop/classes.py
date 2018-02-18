class Emp:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Emp.count += 1

    def displaycount(self):
        print 'total Employee is {}'.format(Emp.count)

    def display_emp(self):
        print 'Name: ', self.name, 'Salary: ', self.salary

emp1 = Emp('sara', 2000)
emp1.display_emp()
emp1.displaycount()
emp2 = Emp('john', 2100)
emp2.display_emp()
emp2.displaycount()
emp3 = Emp('mark', 3400)
emp3.display_emp()
emp3.displaycount()

print Emp.count

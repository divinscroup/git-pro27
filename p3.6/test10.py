import datetime


def outer(msg):
    def inner():
        print(msg)

    return inner


hi = outer('hi')
bye = outer('bye')
hi()
bye()


class Emp:
    count = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mail.com'
        Emp.count += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @classmethod
    def splitter(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'Off Day'
        return 'Work day'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay


class Dev(Emp):
    raise_amount = 1.08

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # super() like Emp.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Emp):
    def __init__(self, first, last, pay, emps=None):
        super().__init__(first, last, pay)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps

    def add_emps(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)

    def del_emps(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)

    def print_emps(self):
        for emp in self.emps:
            print('-->', emp.fullname())

    def __repr__(self):
        return '{} {}, {}'.format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

myDate = datetime.date(2018, 3, 5)
emp1 = Emp('john', 'carter', 5444)
emp2 = Emp('mark', 'cather', 45555)
print(emp1.first)
print(emp2.email)
print(emp2.fullname())
print(emp1.__dict__)
print(Emp.count)
emp3 = 'jack-due-4000'
new_emp3 = Emp.splitter(emp3)
print(new_emp3.first)
print(Emp.is_workday(myDate))
# print(help(Emp))
dev1 = Dev('hanson', 'jonson', 50000, 'js')
dev2 = Dev('sara', 'matthus', 5400, 'C++')
dev3 = Dev('william', 'due', 6000, 'perl')
mngr1 = Manager('adam', 'jones', 10000, [dev1, dev2])
mngr2 = Manager('korey', 'simon', 8000, [dev3])
print(mngr2.email)
print(dev1.__dict__)
dev1.apply_raise()
print(dev1.pay)
mngr1.add_emps(dev3)
mngr1.del_emps(dev1)
print(mngr1.fullname())
mngr1.print_emps()
print(mngr1.__repr__())
print(mngr2.__str__())


class Emp:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@mail.com'.format(self.first, self.last)

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Emp('john', 'dou')
emp1.first = 'lucas'
print(emp1.first)
print(emp1.email)
print(emp1.full_name)

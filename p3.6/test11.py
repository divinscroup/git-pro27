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

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp1 = Emp('john', 'dou')
emp1.first = 'lucas'
emp1.full_name = 'mark due'
print(emp1.first)
print(emp1.email)
print(emp1.full_name)

class Tab:
    menu = {
        'wine': 5,
        'beer': 8,
        'soft_dink': 7,
        'beef': 12,
        'chicken': 11,
        'salad': 10,
        'desert': 9
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def bill(self, tax=13, service=10):
        tax = (tax / 100) * self.total
        service = (service / 100) * self.total
        total = self.total + tax + service

        for item in self.items:
            print(f'{item:20}${self.menu[item]}')
        print(f'{"Total":20}${total:.2f}')


my_order = Tab()
my_order.add('beef')
my_order.add('wine')
my_order.add('salad')
my_order.bill()
my_order.bill(12, 8)

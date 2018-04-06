class Planet:
    speed = 2000

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def speeds(cls):
        return f'planets in solar system are spinning at {cls.speed} miles per hour'


nibrus = Planet('nibrus', 2000, 4.2, 'solar system')
print(f'name is : {nibrus.name}')
print(f'gravity is: {nibrus.gravity}')
print(nibrus.orbit())
print(nibrus.speeds())


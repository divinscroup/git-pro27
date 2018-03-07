
class Members:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name {}\n age {}'.format(self.name, self.age)


class Posts:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return '{}\n{}'.format(self.title, self.content)

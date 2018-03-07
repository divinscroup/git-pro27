import models

member1 = models.Members('John', 33)
member2 = models.Members('Mark', 23)

post1 = models.Posts('title1', 'pos1')
post2 = models.Posts('title2', 'post2')

print member1.__str__()
print post1.__str__()

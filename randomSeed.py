import random
mylist = []

random.seed(0)
for i in xrange(random.randint(1, 10)):
    print i
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
        

print mylist
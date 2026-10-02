import random

print(random.randint(0,100))


print(random.seed(101))

mylist = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(mylist))

print(random.choices(population=mylist, k=10))

random.shuffle(mylist)
print(mylist)


#Problem 1
def squares(n):
    for i in range(n):
        yield i**2

for num in squares(10):
    print(num)

#Problem 2

import random

random.randint(1,10)

def random_number(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

for num in random_number(1,10,12):
    print(num)

#Problem 3
s = "hello"

s = iter(s)
print(next(s))




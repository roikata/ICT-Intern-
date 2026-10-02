from collections import Counter

#counter with list
list = [1,1,2,2,2,2,2,3,4,5,6,7,8,9,10]
print(Counter(list))

#counter with strings
my_string = ("aaabbcdeefffff")
print(Counter(my_string))

#counter with words in sentence
sentence = "How many times does times each each word"

words = sentence.split()

print(Counter(words))

#defaultdict
from collections import defaultdict

d = defaultdict(object)
d["one"]

for item in d:
    print(item)

#namedtuple
from collections import namedtuple

Dog = namedtuple("Dog",["breed", "age","name"])
my_dog = Dog(name = "Sammy",age=2,breed = "Lab")
print(my_dog.name)


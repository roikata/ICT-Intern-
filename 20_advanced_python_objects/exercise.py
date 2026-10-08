#Task1

print(hex(1024))
print(bin(1024))

#Task2
print(round(5.23222,2))

#Task3
s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())

#Task4
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

#Task5

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print(set1.difference(set2))

#Task6
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.union(set2))

#Task7
dict = {x:x ** 2 for x in range(5)}
print(dict)

#Task8
list = [1,2,3,4]
list.reverse()
print(list)

#Task9
list2 = [3,4,2,5,1]
list2.sort()
print(list2)
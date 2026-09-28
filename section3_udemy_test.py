# Arithmetic operators task

(10 * 10) + (5 - 5) + ((2 ** 2 / 16))

#Strings

greet = "hello"
print(greet[1])

#Slicing
string = "Hello"
print(string[::-1]) # Reverse the string using slicing

#two methods of producing the letter 'o' using indexing.
string = "hello"
print(string[-1])

string = "hello"
print(string[4])

#List

my_list = [0,0,0]
my_list = [0] * 3


list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'Goodbye'
print(list3)

#Sorting
list4 = [5,3,4,6,1]
sorted_list = sorted(list4)
print(sorted_list)

#Dictionaries
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2])

#Sets
my_list = [1,2,2,33,4,4,11,22,3,3,2]
my_list = sorted(set(my_list))
print(my_list)
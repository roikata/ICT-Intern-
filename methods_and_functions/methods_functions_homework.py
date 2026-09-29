#First Task
from math import pi

def vol(radius):
    return (4 / 3) * (pi) * (radius ** 3)

print(vol(2))



#calculate the number of upper case letters and lower case letters

def up_low(string):
    up = 0
    low = 0
    for char in string:
        if char.isupper():
            up += 1
        elif char.islower():
            low += 1
    return up, low

print(up_low("Original String"))

#function that takes a list and returns a new list with unique elements

def unique(my_list):
    ordered = []
    for i in my_list:
        if i not in ordered:
            ordered.append(i)
    return ordered


print(unique([1,1,1,1,2,2,3,3,3,3,4,5]))

#multiply all the numbers in a list function

def multiply(my_list):
    result = 1
    for num in my_list:
        result *= num
    return result

print(multiply([1, 2, 3]))

#palindrome

def palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]
print(palindrome("abcba"))



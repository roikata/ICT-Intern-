#LESSER OF TWO EVENS

def lesser_of_two(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)

print(lesser_of_two(2,4))

#ANIMAL CRACKERS

def animal(text):
    words = text.split()
    return words[0][0] == words[1][0]

print(animal("Crazy Kangaroo"))

#MAKES TWENTY

def twenty(num1,num2):
    #return num1 + num2 or num1 == 20 or num2 == 20
    if (num1 + num2 == 20) or num1 == 20 or num2 == 20:
        return True
    else:
        return False


print(twenty(2,3))

#OLD MACDONALD

def capitalize(name):
    return name[:3].capitalize() + name[3:].capitalize()

print(capitalize('macdonald'))

#MASTER YODA

def reversed(text):
    return " ".join(text.split()[::-1])
print(reversed("I am home"))


#first
string = "Print only the words that start with s in this sentence"

for word in string.split():
    if word.startswith("s"):
        print(word)

for num in range(0,11):
    if num % 2 == 0:
        print(num)

#second
divisible_by_3 = [num for num in range(1,51) if num % 3 == 0]
print(divisible_by_3)


#third
string2 = "Print every word in this sentence that has an even number of letters"
for word in string2.split():
    if len(word) % 2 == 0:
        print(word)

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


#fourth
string3 = "Create a list of the letters of every word in this string"
result = [word[0] for word in string3.split()]
print(result)






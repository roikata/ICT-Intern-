#Find 33
def has_33(nums):

    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True

    return False

print(has_33([1,3,3]))

#Paper Doll

def paper_doll(text):
    result = ""

    for char in text:
        result += char * 3

    return result

print(paper_doll("Hello"))


#BLACKJACK

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])

    elif 11 in [a,b,c] and sum([a,b,c]) > 21:
        return sum([a,b,c]) - 10
    else:
        return "BUST"

print(blackjack(9,9,11))

#Summer of 69

def summer_69(nums):

    total = 0
    add = True

    for i in nums:
        while add:
            if i != 6:
                total += i
                break
            else:
                add = False
                total += i
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([1,3,5]))
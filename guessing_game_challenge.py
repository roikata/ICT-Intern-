from random import randint

target = randint(1,100)

print("WELCOME TO THE GUESSING GAME")
print("Rules: ")
print("You have to guess the number between 1 and 100.")
print("Alright...LET'S PLAY!")

guesses = [0]

while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))


    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS! Please try again: ")
        continue

    guesses.append(guess)

    if guess == target:
        print("CONGRATULATIONS, YOU WON!!")
        print(f"You guessed it in only {len(guesses) - 1} guesses!")
        break

    if guesses[-2] == 0:
        if abs(target - guess) <= 10:
            print("WARM!")
        else:
            print("COLD!")

    else:
        if abs(target - guess) < abs(target - guesses[-2]):
            print("WARMER!")
        else:
            print("COLDER!")

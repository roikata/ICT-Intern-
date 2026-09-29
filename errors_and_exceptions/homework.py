#Task 1
def task1():
    try:
        for i in range["a", "b", ["c"]]:
            print(i ** 2)
    except TypeError:
        print("Error")

#Task 2

def task2():
    x = 5
    y = 0

    try:
        z = x / y
        print(z)

    except ZeroDivisionError:
        print("Cannot divide by zero")

    finally:
        print("All Done!")
task2()

#Task 3

def task3():
    while True:
        try:
            number = input("Enter a integer: ")

        except ValueError:
            print("Please enter an integer.")
            continue

        else:
            print(f"Thank you for your time! Your number is {number}.")
            break

task3()

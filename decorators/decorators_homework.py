
def new_decorator(func):
    def wrapper():
        print("Some extra code before the original function")
        func()
        print("Some extra code after the original function")
    return wrapper

@new_decorator
def func_needs_decorator():
    print("I want to be decorated")

print(func_needs_decorator())



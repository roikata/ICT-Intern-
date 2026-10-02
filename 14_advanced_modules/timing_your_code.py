def func_one(num):
    return [str(num) for num in range(num)]

print(func_one(10))

def func_two(num):
    return list(map(str, range(num)))

print(func_two(10))

import time

start = time.time()

result = func_two(100000)
end = time.time() - start
print(end)



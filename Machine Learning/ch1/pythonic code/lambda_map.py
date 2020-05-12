from functools import reduce

f = lambda x, y: x + y
print(f(1, 4))

ex = [1, 2, 3, 4, 5]
f = lambda x: x ** 2
print(list(map(f, ex)))

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(5))

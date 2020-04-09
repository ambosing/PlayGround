from functools import reduce as rd

def plus_ten(x):
    return (x + 10)

def f(x):
    return x > 5 and x < 10

def f2(x, y):
    return (x + y)

print(plus_ten(1))
plus_10 = lambda x: x + 10
print(plus_10(1))

print(list(map(plus_ten, [1, 2, 3])))
print(list(map(plus_10, [1, 2, 3])))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a)))

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x * y, a, b)))

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(f, a)))
print(list(filter(lambda x: x > 5 and x < 10, a)))

a = [1, 2, 3, 4, 5]
print(rd(f2, a))
print(rd(lambda x, y: x + y, a))

files = input().split()
print(list(map(lambda x: x.zfill if len(x.split('.')[0]) < 3 else x, files)))

x = 10
print(locals())

def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

c = calc()
print(c(1), c(2), c(3), c(4), c(5))

def countdown(n):
    i = n + 1
    def minus_one():
        nonlocal i
        i -= 1
        return i
    return minus_one

n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')
def hello():
    print('Hello, world')

def add(a, b):
    print(a + b)

def add2(a, b):
    return (a + b)

def add_sub(a, b):
    return (a + b, a - b)

def add_sub2(a, b):
    return ([a + b, a - b])
hello()
add(3, 4)
res = add2(3, 4)
print(res)
x, y = add_sub(10, 5)
print(x, y)
tu = add_sub(10, 5)
print(tu)
lst = add_sub2(10, 5)
print(lst)

x, y = map(int, input().split())
def calc(x, y):
    return (x + y, x - y, x * y, x / y)

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
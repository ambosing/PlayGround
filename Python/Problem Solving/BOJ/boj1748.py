n = int(input())
x = 10
pre_x = 1
b = 1
result = 0

while x <= n:
    result += (x - pre_x) * b
    pre_x = x
    x *= 10
    b += 1
x //= 10
result += (n + 1 - x) * b
print(result)

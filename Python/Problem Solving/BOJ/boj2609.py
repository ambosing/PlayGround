a, b = map(int, input().split())

c, d = a, b
while b > 0:
    temp = b
    b = a % b
    a = temp
gcd = a
lcd = c * d // gcd

print(gcd, lcd)

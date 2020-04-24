a, b, c = map(int, input().split())
d = int(input())

a += d // 3600
b += (d % 3600) // 60
c += d % 60

if c >= 60:
    b += c // 60
    c %= 60

if b >= 60:
    a += b // 60
    b %= 60

if a >= 24:
    a %= 24

print(a, b, c)
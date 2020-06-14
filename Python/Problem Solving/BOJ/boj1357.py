a, b = input().split()

a = a[::-1]
b = b[::-1]
ab = int(a) + int(b)
ab = str(ab)[::-1]
print(int(ab))

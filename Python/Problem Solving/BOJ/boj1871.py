t = int(input())

for i in range(t):
    s, v = input().split("-")
    v2 = 0
    mul = 26 ** 2
    v = int(v)
    for c in s:
        v2 += mul * (ord(c) - 65)
        mul //= 26
    if abs(v2 - v) <= 100:
        print("nice")
    else:
        print("not nice")

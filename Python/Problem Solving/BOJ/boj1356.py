n = input()

for i in range(1, len(n)):
    n1 = n[:i]
    n2 = n[i:]
    res1 = 1
    res2 = 1
    for j in n1:
        res1 *= int(j)
    for j in n2:
        res2 *= int(j)
    if res1 == res2:
        print("YES")
        break
else:
    print("NO")

res = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b == c:
        num = 10000 + a * 1000
    elif a == b or b == c:
        num = 1000 + 100 * b
    elif a == c:
        num = 1000 + 100 * b
    else:
        num = max(a, b, c) * 100
    res.append(num)
print(max(res))

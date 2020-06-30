n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    result = (abs(b - a) + 1) * (a + b) // 2
    print("Scenario #%d:\n%d" % (i + 1, result))
    if i != n - 1:
        print()
n, m = map(int, input().split())
a = []

for _ in range(n):
    a.append(int(input()))

for i in range(1, m + 1):
    for j in range(n - 1):
        if a[j] % i > a[j + 1] % i:
            a[j], a[j + 1] = a[j + 1], a[j]
print("\n".join(map(str, a)))


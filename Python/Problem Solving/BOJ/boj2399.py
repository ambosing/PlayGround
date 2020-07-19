n = int(input())
lst = list(map(int, input().split()))
res = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        res += abs(lst[i] - lst[j])
print(res * 2)

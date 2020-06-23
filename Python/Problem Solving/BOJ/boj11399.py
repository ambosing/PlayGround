n = int(input())
lst = list(map(int, input().split()))
lst.sort()
result = 0
for i in range(len(lst)):
    for j in range(i + 1):
        result += lst[j]
print(result)

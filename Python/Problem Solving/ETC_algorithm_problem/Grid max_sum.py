lst = []
max_val = -1
n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    lst.append(nums)
    max_val = max(sum(nums), max_val)

for i in range(n):
    hap = 0
    for j in range(n):
        hap += lst[j][i]
    max_val = max(max_val, hap)
hap = 0
for j in range(n):
    hap += lst[j][j]
max_val = max(max_val, hap)
hap = 0
for j in range(n):
    hap += lst[j][n - j - 1]
max_val = max(max_val, hap)

print(max_val)

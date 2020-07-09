import sys

n = int(input())
lst = list(map(int, input().split()))
avg = round(sum(lst) / n)
idx = 0
min_val = sys.maxsize

for i in range(n):
    val = abs(avg - lst[i])
    if val < min_val:
        min_val = val
        idx = i
    if val == min_val and lst[i] > lst[idx]:
        idx = i
print(avg, idx + 1)

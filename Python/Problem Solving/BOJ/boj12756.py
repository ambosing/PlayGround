import sys

n = int(input())
res = 0
i = n + 1
max_val = sys.maxsize
while i < max_val:
    d = divmod(i, n)
    if d[0] >= n:
        break
    if d[0] == d[1]:
        res += i
        i += n
        continue
    i += 1
print(res)

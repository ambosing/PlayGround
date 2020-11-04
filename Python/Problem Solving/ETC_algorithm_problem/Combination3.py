from itertools import combinations
from sys import stdout

n, m = map(int, input().split())
lst = [str(i) for i in range(1, n + 1)]
cnt = 0
for i in list(combinations(lst, m)):
    stdout.write(" ".join(i) + "\n")
    cnt += 1
print(cnt)

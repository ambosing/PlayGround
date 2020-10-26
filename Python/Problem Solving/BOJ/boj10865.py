from collections import defaultdict
import sys


dic = defaultdict(int)
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[a] += 1
    dic[b] += 1

for k in range(1, n + 1):
    sys.stdout.write(str(dic[k]) + "\n")

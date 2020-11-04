from itertools import permutations
from sys import stdout


n, m = map(int, input().split())
lst = [str(i) for i in range(1, n + 1)]
cnt = 0
for item in list(permutations(lst, m)):
    stdout.write(" ".join(item) + "\n")
    cnt += 1
stdout.write(str(cnt))

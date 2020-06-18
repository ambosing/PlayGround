from functools import cmp_to_key
import sys


def compare(x, y):
    len_x = len(x)
    len_y = len(y)

    if len_x > len_y:
        return 1
    elif len_x == len_y:
        for idx in range(len_x):
            if x[idx] != y[idx]:
                return ord(x[idx]) - ord(y[idx])
        return 0
    elif len_x < len_y:
        return -1


n = int(input())
lst = []
for i in range(n):
    inp = sys.stdin.readline().rstrip()
    chk = 1
    for s in lst:
        if s == inp:
            chk = 0
    if chk == 1:
        lst.append(inp)

lst = sorted(lst, key=cmp_to_key(compare))
sys.stdout.write('\n'.join(lst))

import sys
from functools import cmp_to_key


def xy_compare(x, y):
    if x[1] > y[1]:
        return 1
    elif x[1] == y[1]:
        if x[0] > y[0]:
            return 1
        elif x[0] < y[0]:
            return -1
        else:
            return 0
    else:
        return -1


xy_lst = []
t = int(input())

for i in range(t):
    xy_lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

xy_lst = sorted(xy_lst, key=cmp_to_key(xy_compare))
for item in xy_lst:
    sys.stdout.write(str(item[0]) + " " + str(item[1]) + "\n")


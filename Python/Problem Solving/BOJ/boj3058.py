import sys

t = int(input())

for i in range(t):
    lst = list(map(int, input().split()))
    hap = 0
    min_val = sys.maxsize
    for item in lst:
        if item % 2 == 0:
            hap += item
            min_val = item if min_val > item else min_val
    print(hap, min_val)

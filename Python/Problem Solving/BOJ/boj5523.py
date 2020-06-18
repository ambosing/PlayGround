import sys

n = int(input())
a_cnt = 0
b_cnt = 0

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a > b:
        a_cnt += 1
    elif b > a:
        b_cnt += 1
print(a_cnt, b_cnt)

import sys

t = int(input())

for i in range(t):
    num = int(sys.stdin.readline())
    lst = []
    while num > 0:
        lst.append(num % 2)
        num //= 2
    for idx in range(len(lst)):
        if lst[idx] == 1:
            sys.stdout.write(str(idx) + " ")

import sys

n = int(input())

for i in range(n):
    lst = list(sys.stdin.readline())
    if lst[0].islower():
        lst[0] = chr(ord(lst[0]) - 32)
    s = ''.join(lst)
    sys.stdout.write(s)

import sys


t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        for ii in range(n):
            if ii != 0 and ii != n - 1 and j != 0 and j != n - 1:
                sys.stdout.write("J")
            else:
                sys.stdout.write("#")
        print()
    if i != t - 1:
        print()

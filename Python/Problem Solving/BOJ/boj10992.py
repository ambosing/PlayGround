import sys

n = int(input())

for i in range(n):
    if i == 0:
        for j in range(n - 1):
            sys.stdout.write(" ")
        sys.stdout.write("*")
    elif i == n - 1:
        limit = 2 * n - 1
        for j in range(limit):
            sys.stdout.write("*")
    else:
        limit = n + i - 1
        limit2 = n - (i + 1)
        for j in range(limit):
            if j < limit2:
                sys.stdout.write(" ")
            elif j == limit2:
                sys.stdout.write("*")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("*")
    sys.stdout.write("\n")

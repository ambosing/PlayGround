import sys

n = int(input())

for i in range(n):
    if i == 0:
        limit = n - 1
        for j in range(limit):
            sys.stdout.write(" ")
        sys.stdout.write("*\n")
    else:
        limit = n - i - 1
        for j in range(limit):
            sys.stdout.write(" ")
        sys.stdout.write("*")
        for j in range(2 * (i - 1) + 1):
            sys.stdout.write(" ")
        sys.stdout.write("*\n")

import sys

n = int(input())
a = input()
m = int(input())
b = input()
ab = a + " " + b
ab = list(map(int, ab.split()))
ab.sort()
for i in range(n + m):
    if i != n + m - 1:
        sys.stdout.write(str(ab[i]) + " ")
    else:
        sys.stdout.write(str(ab[i]) + "\n")

import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split(","))
    sys.stdout.write(str(a + b) + "\n")

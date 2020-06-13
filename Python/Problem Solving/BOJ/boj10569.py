import sys

n = int(input())

for i in range(n):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    result = e - v + 2
    sys.stdout.write(str(result) + "\n")

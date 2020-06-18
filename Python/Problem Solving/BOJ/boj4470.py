import sys
n = int(input())

for i in range(n):
    s = sys.stdin.readline()
    sys.stdout.write(str(i + 1) + ". " + s)

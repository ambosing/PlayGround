import sys

n = input()
a = [0]
hap = 0
for i in map(int, input().split()):
    hap += i
    a.append(hap)
for _ in range(int(input())):
    s, e = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(a[e] - a[s-1]) + "\n")


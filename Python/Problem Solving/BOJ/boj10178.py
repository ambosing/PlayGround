import sys

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    div = a // b
    mod = a % b
    sys.stdout.write("You get " + str(div) + " piece(s) and your dad gets " + str(mod) + " piece(s).\n")

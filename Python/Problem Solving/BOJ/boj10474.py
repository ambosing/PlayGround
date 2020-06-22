import sys

while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 and b == 0:
        break
    div = a // b
    mod = a % b
    sys.stdout.write(str(div) + " " + str(mod) + " / " + str(b) + "\n")

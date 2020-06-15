import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().rstrip().split())
    except:
        break
    sys.stdout.write(str(a + b) + "\n")

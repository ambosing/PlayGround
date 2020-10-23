import sys


r, c = map(int, input().split())
a, b = map(int, input().split())
row = r * a
col = c * b
for i in range(row):
    k = i // a
    for j in range(col):
        t = j // b
        if k % 2 == 0 and t % 2 == 0:
            sys.stdout.write("X")
        elif k % 2 == 1 and t % 2 == 1:
            sys.stdout.write("X")
        else:
            sys.stdout.write(".")
    sys.stdout.write("\n")


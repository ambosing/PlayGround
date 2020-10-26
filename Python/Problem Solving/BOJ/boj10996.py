import sys


n = int(input())

n2 = n * 2
for i in range(n2):
    if i % 2 == 0:
        a, b = "*", " "
    else:
        a, b = " ", "*"
    for j in range(n):
        if j % 2 == 0:
            sys.stdout.write(a)
        else:
            sys.stdout.write(b)

    sys.stdout.write("\n")

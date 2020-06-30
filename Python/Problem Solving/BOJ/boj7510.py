from math import sqrt

n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    chk = False
    aa = a ** 2
    bb = b ** 2
    cc = c ** 2
    if sqrt(aa + bb) == c:
        chk = True
    elif sqrt(aa + cc) == b:
        chk = True
    elif sqrt(bb + cc) == a:
        chk = True
    if chk:
        print("Scenario #%d:\nyes" % (i + 1))
    else:
        print("Scenario #%d:\nno" % (i + 1))
    if i != n - 1:
        print()

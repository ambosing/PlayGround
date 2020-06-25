from math import sqrt

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    aa = a ** 2
    bb = b ** 2
    cc = c ** 2
    if sqrt(aa + bb) == c or sqrt(bb + cc) == a or sqrt(cc + aa) == b:
        print("right")
    else:
        print("wrong")

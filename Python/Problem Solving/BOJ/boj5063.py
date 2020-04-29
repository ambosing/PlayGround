from sys import stdin

n = int(input())

for i in range(n):
    r, e, c = map(int, stdin.readline().split())
    if e - c == r:
        print("does not matter")
    elif e - c > r:
        print("advertise")
    elif e - c < r:
        print("do not advertise")

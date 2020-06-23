import sys

t = int(input())

for i in range(t):
    a_cnt = 0
    b_cnt = 0
    n = int(input())
    for j in range(n):
        a, b = sys.stdin.readline().rstrip().split()
        if a == "R" and b == "S":
            a_cnt += 1
        elif b == "R" and a == "S":
            b_cnt += 1
        elif a == "S" and b == "P":
            a_cnt += 1
        elif b == "S" and a == "P":
            b_cnt += 1
        elif a == "P" and b == "R":
            a_cnt += 1
        elif b == "P" and a == "R":
            b_cnt += 1
    if a_cnt > b_cnt:
        print("Player 1")
    elif b_cnt > a_cnt:
        print("Player 2")
    else:
        print("TIE")

import sys


def is_exist(lst, item):
    for i in lst:
        if i == item:
            return True
    return False


t = int(input())

for i in range(t):
    m, target = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0
    seat_lst = []
    for j in range(m):
        seat = int(sys.stdin.readline().rstrip())
        cnt += 1
        if not is_exist(seat_lst, seat):
            seat_lst.append(seat)
    print(cnt - len(seat_lst))

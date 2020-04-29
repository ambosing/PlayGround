from sys import stdin

n = int(input())

cnt = [0, 0, 0, 0, 0]
for i in range(n):
    a, b = map(int, stdin.readline().split())
    if a == 0 or b == 0:
        cnt[4] += 1
    elif a > 0 and b > 0:
        cnt[0] += 1
    elif b > 0 > a:
        cnt[1] += 1
    elif a < 0 and b < 0:
        cnt[2] += 1
    elif a > 0 > b:
        cnt[3] += 1

for i in range(1, 6):
    if i < 5:
        print("Q%d: %d" % (i, cnt[i - 1]))
    else:
        print("AXIS: %d" % cnt[i - 1])

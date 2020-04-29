from sys import stdin

t = int(input())

one_cnt = 0
zero_cnt = 0
for i in range(t):
    temp = stdin.readline()
    if temp == "1\n":
        one_cnt += 1
    else:
        zero_cnt += 1

if one_cnt < zero_cnt:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")

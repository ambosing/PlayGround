from string import ascii_uppercase
import sys


def check(cnt, name):
    odd_cnt = 0
    for ii, val in enumerate(cnt):
        if val % 2 == 1:
            odd_cnt += 1
        if odd_cnt >= 2:
            return False
    if len(name) % 2 == 1:
        return True
    return False


def check2(cnt):
    for val in cnt:
        if val % 2 == 1:
            return False
    return True


alpha = list(ascii_uppercase)
s = input()
lst = [0] * 26
for c in s:
    idx = alpha.index(c)
    lst[idx] += 1
if check2(lst):
    for i, v in enumerate(lst):
        for _ in range(v // 2):
            sys.stdout.write(alpha[i])
    for i in range(len(lst) - 1, -1, -1):
        v = lst[i]
        for _ in range(v // 2):
            sys.stdout.write(alpha[i])
elif check(lst, s):
    idx = 0
    for i, v in enumerate(lst):
        if v % 2 == 1:
            idx = i
        for _ in range(v // 2):
            sys.stdout.write(alpha[i])
    sys.stdout.write(alpha[idx])
    for i in range(len(lst) - 1, -1, -1):
        for _ in range(lst[i] // 2):
            sys.stdout.write(alpha[i])
else:
    print("I'm Sorry Hansoo")



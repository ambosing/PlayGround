from collections import deque

nec = input()
for i in range(int(input())):
    s = deque(input())
    res = ""
    while s:
        c = s.popleft()
        if c in nec and c not in res:
            res += c
    if nec == res:
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))

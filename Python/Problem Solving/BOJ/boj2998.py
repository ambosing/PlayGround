import sys
from collections import deque

s = input()
deque = deque()
cnt = 0
hap = 0
mul_num = [1, 4, 2]
s_len = len(s)
if s_len % 3 == 1:
    s = "00" + s
elif s_len % 3 == 2:
    s = "0" + s

for i in range(len(s) - 1, -1, -1):
    cnt += 1
    if cnt == 3:
        hap += mul_num[(i + 1) % 3] * int(s[i])
        deque.appendleft(str(hap))
        cnt = 0
        hap = 0
        continue
    hap += mul_num[(i + 1) % 3] * int(s[i])

print(''.join(deque))

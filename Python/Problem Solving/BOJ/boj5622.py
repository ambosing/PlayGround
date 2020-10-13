import string
from collections import deque

alpha_up = deque(string.ascii_uppercase)
dic = dict()
for i in range(1, 10):
    k = 3
    if i == 1:
        continue
    elif i == 7 or i == 9:
        k = 4
    for _ in range(k):
        dic[alpha_up.popleft()] = i

s = input()
res = 0
for c in s:
    res += dic[c] + 1
print(res)

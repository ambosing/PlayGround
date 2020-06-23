import string
import sys

alpha_low = list(string.ascii_lowercase)
lst = [0] * 26
ss = sys.stdin.readlines()

for s in ss:
    s = s.rstrip()
    for c in s:
        if c == ' ':
            continue
        idx = alpha_low.index(c)
        lst[idx] += 1

max_val = max(lst)
for i in range(26):
    if max_val == lst[i]:
        sys.stdout.write(alpha_low[i])

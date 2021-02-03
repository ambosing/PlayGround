from string import ascii_lowercase
import sys


def dfs(r):
    if len(s) == r:
        sys.stdout.write(''.join(res) + "\n")
    else:
        for i in range(26):
            if alpha_cnt[i] > 0:
                alpha_cnt[i] -= 1
                res[r] = alpha[i]
                dfs(r + 1)
                alpha_cnt[i] += 1


alpha = ascii_lowercase
for _ in range(int(input())):
    s = sys.stdin.readline().rstrip()
    alpha_cnt = [0] * 26
    for item in s:
        idx = alpha.index(item)
        alpha_cnt[idx] += 1
    res = [""] * len(s)
    dfs(0)

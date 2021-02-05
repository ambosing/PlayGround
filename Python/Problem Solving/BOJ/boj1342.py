from string import ascii_lowercase


def dfs(d):
    global cnt
    if d == len(s):
        for i in range(d - 1):
            if a[i] == a[i + 1]:
                break
        else:
            cnt += 1
    else:
        for i in range(26):
            if alpha_cnt[i] > 0:
                alpha_cnt[i] -= 1
                a[d] = alpha[i]
                dfs(d + 1)
                alpha_cnt[i] += 1


s = input()
alpha = list(ascii_lowercase)
alpha_cnt = [0] * 26
cnt = 0
a = [""] * len(s)
for c in s:
    idx = alpha.index(c)
    alpha_cnt[idx] += 1
max_val = max(alpha_cnt)
if sum(alpha_cnt) - max_val + 1 < max_val:
    print(0)
else:
    dfs(0)
    print(cnt)


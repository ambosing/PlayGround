import string

alpha_low = string.ascii_lowercase
t = int(input())
result = 0

for i in range(t):
    s = input()
    alpha_count = [0] * 26
    len_s = len(s)
    cnt = 1
    for j in range(len_s):
        idx = alpha_low.index(s[j])
        if alpha_count[idx] == 0:
            alpha_count[idx] += 1
        else:
            chk = False
            same_idx = -1
            for k in range(j):
                if s[k] == s[j]:
                    same_idx = k
                    chk = True
            if chk and j - same_idx > 1:
                cnt = 0
    result += cnt
print(result)

from string import ascii_uppercase


def dfs(a, alpha):
    global cnt, lst
    if a >= m:
        lst.append(alpha)
        cnt += 1
    else:
        if int(n[a]) == 0:
            return
        dfs(a + 1, alpha + alpha_up[int(n[a]) - 1])
        val = int(n[a:a+2])
        if a < m - 1 and val <= 26:
            dfs(a + 2, alpha + alpha_up[val - 1])


alpha_up = ascii_uppercase
n = input()
m = len(n)
cnt = 0
lst = []
dfs(0, "")
lst.sort()
print("\n".join(lst) + "\n" + str(cnt))

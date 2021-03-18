from string import ascii_uppercase


def dfs(a):
    global cnt
    if a == len(c):
        print(''.join(res))
        cnt += 1
    else:
        if c[a] == '0':
            return
        res.append(alpha[int(c[a]) - 1])
        dfs(a + 1)
        res.pop()
        if a < len(c) - 1 and int(c[a:a+2]) <= 26:
            idx = int(c[a:a+2]) - 1
            res.append(alpha[idx])
            dfs(a + 2)
            res.pop()


c = input()
alpha = list(ascii_uppercase)
res = []
cnt = 0
dfs(0)
print(cnt)

def func_1(n):
    for i, v in enumerate(n):
        if i < len(n) - 1 and n[i + 1] == '1':
            for j in range(i + 2, len(n)):
                if n[j] == '1':
                    break
            else:
                return func_2(n, i)
    return n


def func_2(n, i):
    n = list(n)
    if n[i] == '0':
        n[i] = '1'
    else:
        n[i] = '0'
    return "".join(n)


def is_all_zero(n):
    for v in n:
        if v != '0':
            return False
    return True


def dfs(n, c, d):
    k = "".join(n)
    if is_all_zero(n):
        if k not in d.keys() or d[k] >= c:
            d[k] = c
            dfs(func_1(n), c + 1, d)
            dfs(func_2(n, -1), c + 1, d)
    if k not in d.keys() or d[k] >= c:
        d[k] = c
        dfs(func_1(n), c + 1, d)
        dfs(func_2(n, -1), c + 1, d)
        return


x = bin(int(input()))[2:]
dic = {x: 0}
dfs(x, 0, dic)
key = "0" * len(x)
print(dic[key])

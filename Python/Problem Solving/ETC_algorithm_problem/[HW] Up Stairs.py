def func(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    if dp[a] != 0:
        return dp[a]
    dp[a] = func(a - 1) + func(a - 2)
    return dp[a]


n = int(input())
dp = [0] * 47
res = func(n)
print(res)

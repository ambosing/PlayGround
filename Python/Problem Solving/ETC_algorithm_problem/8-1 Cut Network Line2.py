def memo(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    if dp[a] != 0:
        return dp[a]
    else:
        dp[a] = memo(a - 1) + memo(a - 2)
    return dp[a]


n = int(input())
dp = [0] * 47
res = memo(n)
print(res)

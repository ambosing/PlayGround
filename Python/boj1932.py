n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

max_val = 0
for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
        max_val = max(max_val, dp[i][j])
print(max_val)

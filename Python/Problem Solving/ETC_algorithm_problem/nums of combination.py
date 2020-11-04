def dfs(a, s, hap):
    global cnt
    if a == m:
        if hap % k == 0:
            cnt += 1
    else:
        for i in range(s, n):
            dfs(a + 1, i + 1, hap + nums[i])


n, m = map(int, input().split())
nums = list(map(int, input().split()))
k = int(input())
cnt = 0
dfs(0, 0, 0)
print(cnt)

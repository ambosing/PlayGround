def dfs(a):
    global cnt
    if a == m:
        cnt += 1
        print(' '.join(nums))
        return
    else:
        for i in range(1, n + 1):
            nums[a] = str(i)
            dfs(a + 1)


cnt = 0
n, m = map(int, input().split())
nums = [0] * m
dfs(0)
print(cnt)

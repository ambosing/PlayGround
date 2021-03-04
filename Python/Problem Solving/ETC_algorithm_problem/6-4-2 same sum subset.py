def dfs(a):
    if a >= n:
        sum1 = 0
        sum2 = 0
        for i in range(n):
            if v[i]:
                sum1 += nums[i]
            else:
                sum2 += nums[i]
        if sum1 == sum2:
            print("YES")
            exit(0)
    else:
        dfs(a + 1)
        v[a] = False
        dfs(a + 1)
        v[a] = True


n = int(input())
nums = list(map(int, input().split()))
v = [True] * n
dfs(0)
print("NO")

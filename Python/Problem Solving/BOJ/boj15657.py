def dfs(a):
    if a == m:
        s = " ".join(list(map(str, lst)))
        print(s)
        return
    for i in range(n):
        if a == 0 or (a > 0 and lst[a - 1] <= nums[i]):
            lst[a] = nums[i]
            dfs(a + 1)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = [0] * m
dfs(0)


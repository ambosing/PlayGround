def dfs(a, b):
    if a == k:
        if 1 <= b <= s:
            nums.add(b)
    else:
        dfs(a + 1, b + w[a])
        dfs(a + 1, b - w[a])
        dfs(a + 1, b)


k = int(input())
w = list(map(int, input().split()))
s = sum(w)
nums = set()
check = [0] * (s + 1)
dfs(0, 0)
print(s - len(nums))
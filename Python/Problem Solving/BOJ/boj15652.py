def dfs(a):
    if a == m:
        s = " ".join(map(str, lst))
        answer.append(s)
        return
    for i in range(n):
        if a == 0 or (a > 0 and lst[a - 1] <= nums[i]):
            lst[a] = nums[i]
            dfs(a + 1)


n, m = map(int, input().split())
nums = [i + 1 for i in range(n)]
lst = [0] * m
answer = []
dfs(0)
print("\n".join(answer))

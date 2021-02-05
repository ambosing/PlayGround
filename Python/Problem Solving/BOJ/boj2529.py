def comp(a, b, c):
    if c == '<':
        if a < b:
            return True
    if c == '>':
        if a > b:
            return True
    return False


def dfs(a):
    if a == k + 1:
        copy_nums = nums.copy()
        copy_nums = map(str, copy_nums)
        res.append(''.join(copy_nums))
    else:
        for i in range(10):
            if not v[i]:
                if a == 0 or comp(nums[a - 1], i, lst[a - 1]):
                    v[i] = True
                    nums[a] = i
                    dfs(a + 1)
                    v[i] = False


k = int(input())
lst = list(input().split())
nums = [0] * (k + 1)
v = [False] * 10
res = []
dfs(0)
res.sort()
print(res[-1] + "\n" + res[0])

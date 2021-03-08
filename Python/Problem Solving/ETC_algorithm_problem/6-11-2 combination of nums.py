def comb(a, s, res):
    global cnt
    if a == k:
        if res % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            if not used[i]:
                used[i] = True
                comb(a + 1, i + 1, res + nums[i])
                used[i] = False


n, k = map(int, input().split())
nums = list(map(int, input().split()))
m = int(input())
used = [False] * n
nums.sort()
cnt = 0
comb(0, 0, 0)
print(cnt)

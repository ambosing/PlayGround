n = int(input())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0
res = 0
for i in nums:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0
print(res)


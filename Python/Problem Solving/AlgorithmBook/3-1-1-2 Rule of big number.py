n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
div = m // (k + 1)
rem = m % (k + 1)
res = div * (nums[0] * k + nums[1])
res += rem * nums[0]
print(res)

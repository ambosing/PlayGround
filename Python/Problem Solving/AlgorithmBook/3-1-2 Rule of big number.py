n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
cnt = m // (k + 1) * k
cnt += m % (k + 1)

res = cnt * nums[-1]
res += (m - cnt) * nums[-2]
print(res)

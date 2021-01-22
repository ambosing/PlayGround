import sys

for i in range(int(input())):
    n, s, e, k = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))[s - 1:e]
    nums.sort()
    print("#%d %d" % (i + 1, nums[k - 1]))

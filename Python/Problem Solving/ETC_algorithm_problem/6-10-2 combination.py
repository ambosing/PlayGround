def comb(lst, s):
    global cnt
    if len(lst) == m:
        print(" ".join(lst))
        cnt += 1
    else:
        for i in range(s, n):
            if not used[i]:
                if i == 0 or nums[i - 1] != nums[i] or used[i - 1]:
                    lst.append(nums[i])
                    used[i] = True
                    comb(lst, i + 1)
                    used[i] = False
                    lst.pop()


n, m = map(int, input().split())
cnt = 0
nums = ["1", "9", "4", "6", "5", "8"]
nums.sort()
used = [False] * n
comb([], 0)
print(cnt)

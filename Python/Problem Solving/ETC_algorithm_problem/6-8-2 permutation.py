def permutation(lst):
    global cnt
    if len(lst) == r:
        cnt += 1
        print(" ".join(lst))
    else:
        for i in range(len(nums)):
            if not used[i] or i == 0 or lst[i-1] != lst[i] or used[i-1]:
                lst.append(str(nums[i]))
                used[i] = True
                permutation(lst)
                used[i] = False
                lst.pop()


n, r = map(int, input().split())
nums = [i + 1 for i in range(n)]
cnt = 0
used = [False] * n
permutation([])

print(cnt)

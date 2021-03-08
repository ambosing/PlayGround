def perm_predict(lst):
    if len(lst) == n:
        val = 0
        for i in range(n):
            val += int(lst[i]) * comb(n - 1, i)
        if val == f:
            print(" ".join(lst))
            exit(0)

    else:
        for i in range(n):
            if not used[i]:
                lst.append(str(nums[i]))
                used[i] = True
                perm_predict(lst)
                used[i] = False
                lst.pop()


def comb(a, r):
    r1 = max(a - r, r)
    r2 = min(a - r, r)
    nums1 = 1
    nums2 = 1
    for i in range(a, r1, -1):
        nums1 *= i
    for i in range(r2, 1, -1):
        nums2 *= i
    return nums1 // nums2


n, f = map(int, input().split())
nums = [i + 1 for i in range(n)]
used = [False] * n

perm_predict([])

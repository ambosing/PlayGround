n, k = map(int, input().split())
nums = list(map(int, input().split()))


def k_big_num(a):
    lst = []
    for i in range(len(a) - 2):
        for j in range(i + 1, len(a) - 1):
            for t in range(j + 1, len(a)):
                lst.append(a[i] + a[j] + a[t])
    lst = list(set(lst))
    lst.sort(reverse=True)
    print(lst[k - 1])


k_big_num(nums)

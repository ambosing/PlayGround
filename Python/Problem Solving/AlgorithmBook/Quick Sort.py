def quick_sort(a, s, e):
    if s >= e:
        return
    p = s
    lt = p + 1
    rt = e
    while lt <= rt:
        while lt <= e and a[lt] <= a[p]:
            lt += 1
        while rt > s and a[rt] >= a[p]:
            rt -= 1
        if rt < lt:
            a[rt], a[p] = a[p], a[rt]
        else:
            a[rt], a[lt] = a[lt], a[rt]
    quick_sort(a, s, rt - 1)
    quick_sort(a, rt + 1, e)


def quick_sort2(a):
    if len(a) <= 1:
        return a
    p = 0
    tail = a[1:]
    lt_lst = [x for x in tail if x <= a[p]]
    rt_lst = [x for x in tail if x > a[p]]
    return quick_sort2(lt_lst) + [a[p]] + quick_sort2(rt_lst)


lst = [5, 4, 9, 0, 3, 1, 6, 2, 7, 8]
lst2 = [5, 4, 9, 0, 3, 1, 6, 2, 7, 8]
quick_sort(lst, 0, len(lst) - 1)
lst2 = quick_sort2(lst2)
print(lst)
print(lst2)


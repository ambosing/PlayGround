k = int(input())

for i in range(k):
    lst = list(map(int, input().split()))
    max_gap = 0
    len_lst = lst[0]
    lst.pop(0)
    lst.sort(reverse=True)
    for idx in range(len_lst):
        if idx == 0:
            continue
        gap = abs(lst[idx - 1] - lst[idx])
        max_gap = gap if max_gap < gap else max_gap
    print("Class %d" % (i + 1))
    print("Max %d, Min %d, Largest gap %d" % (max(lst), min(lst), max_gap))

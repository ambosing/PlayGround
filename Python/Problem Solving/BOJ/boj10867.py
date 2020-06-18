import sys

n = int(input())
lst = list(map(int, input().split()))
sort_lst = []
for i in lst:
    chk = True
    for item in sort_lst:
        if i == item:
            chk = False
    if chk:
        sort_lst.append(i)

sort_lst = sorted(sort_lst)
len_sort_lst = len(sort_lst)
for i in range(len_sort_lst):
    if len_sort_lst - 1 == i:
        sys.stdout.write((str(sort_lst[i])))
        break
    sys.stdout.write(str(sort_lst[i]) + " ")

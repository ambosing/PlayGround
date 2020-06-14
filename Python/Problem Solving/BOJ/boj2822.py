idx_lst = []
hap = 0
lst = []

for i in range(8):
    lst.append(int(input()))

sort_lst = sorted(lst)[::-1]
for i in range(5):
    hap += sort_lst[i]
    idx_lst.append(lst.index(sort_lst[i]))

print(hap)
idx_lst.sort()
for i in idx_lst:
    print(i + 1, end=" ")

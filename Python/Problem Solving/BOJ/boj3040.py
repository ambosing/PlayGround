lst = []
for i in range(9):
    lst.append(int(input()))

len_lst = len(lst)
hap = sum(lst)
chk = 0
for i in range(len_lst):
    for j in range(len_lst):
        if i == j:
            continue
        if hap - lst[i] - lst[j] == 100:
            chk = 1
            lst[i] = -1
            lst[j] = -1
    if chk == 1:
        break
for i in lst:
    if i != -1:
        print(i)

lst = list(input())

pre = lst[0]
res = 10
lst_len = len(lst)
for i in range(1, lst_len):
    if pre == lst[i]:
        res += 5
    else:
        res += 10
    pre = lst[i]
print(res)

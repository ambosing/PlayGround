def is_kin(lst_):
    lst2 = lst_.copy()
    max_val = max(lst_)
    min_val = min(lst_)
    lst2.remove(max_val)
    lst2.remove(min_val)
    len_lst = len(lst2)

    for idx in range(len_lst):
        for j in range(len_lst):
            if abs(lst2[idx] - lst2[j]) >= 4:
                return True
    return False


t = int(input())

for i in range(t):
    lst = list(map(int, input().split()))
    if is_kin(lst):
        print("KIN")
        continue
    print(sum(lst) - min(lst) - max(lst))

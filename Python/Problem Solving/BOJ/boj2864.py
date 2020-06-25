def max_change_value(val, lst_val):
    for i in range(len(val)):
        if val[i] == "5":
            val[i] = "6"
    lst_val.append(int(''.join(val)))
    return lst_val


def min_change_value(val, lst_val):
    for i in range(len(val)):
        if val[i] == "6":
            val[i] = "5"
    lst_val.append(int(''.join(val)))
    return lst_val


a, b = input().split()
a, b = list(a), list(b)
lst = []
lst = max_change_value(a, lst)
lst = min_change_value(a, lst)
lst = max_change_value(b, lst)
lst = min_change_value(b, lst)
max_val = lst[0] + lst[2]
min_val = lst[1] + lst[3]
print(min_val, max_val)

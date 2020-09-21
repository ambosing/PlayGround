x = int(input())
lst = [64]
sum_lst = 64
if x == 64:
    print(1)
else:
    while True:
        val = lst.pop() // 2
        lst.append(val)
        sum_lst = sum(lst)
        if sum_lst == x:
            break
        lst.append(val)
        if sum_lst > x:
            lst.pop()
    print(len(lst))

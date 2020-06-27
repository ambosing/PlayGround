for _ in range(int(input())):
    n = int(input())
    hap = 0
    lst = []
    max_val = 0
    chk = 0
    for _ in range(n):
        i = int(input())
        lst.append(i)
        max_val = i if max_val < i else max_val
        hap += i
    for i in lst:
        if i == max_val:
            chk += 1
    if chk > 1:
        print("no winner")
    elif chk == 1 and max_val > hap // 2:
        print("majority winner %d" % (lst.index(max_val) + 1))
    elif chk == 1 and max_val <= hap // 2:
        print("minority winner %d" % (lst.index(max_val) + 1))
    
    

from sys import stdin

while True:
    lst = []
    a = int(stdin.readline().rstrip('\n'))
    if a == -1:
        break
    for i in range(1, a):
        if a % i == 0:
            lst.append(i)
    if sum(lst) == a:
        print("%d = " % a, end="")
        len_lst = len(lst)
        for i in range(len_lst):
            if i != len_lst - 1:
                print("%d + " % lst[i], end="")
            else:
                print("%d" % lst[i])
    else:
        print("%d is NOT perfect." % a)

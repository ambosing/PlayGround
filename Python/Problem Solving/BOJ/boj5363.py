for _ in range(int(input())):
    lst = input().split()
    lst.append(lst.pop(0))
    lst.append(lst.pop(0))
    print(' '.join(lst))

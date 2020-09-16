for _ in range(int(input())):
    lst = input().split()
    if "Simon" in lst and "says" in lst:
        print(' ' + ' '.join(lst[2:]))

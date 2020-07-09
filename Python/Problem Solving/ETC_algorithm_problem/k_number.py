for i in range(int(input())):
    n, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = lst[s - 1:e]
    lst.sort()
    print("#%d %d" % (i + 1, lst[k - 1]))

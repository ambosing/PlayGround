for _ in range(int(input())):
    s, p = input().split()
    res = len(s) - (len(p) - 1) * s.count(p)
    print(res)

for i in range(int(input())):
    s = input().lower()
    if s[::-1] == s:
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))

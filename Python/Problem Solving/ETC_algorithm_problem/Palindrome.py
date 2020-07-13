for i in range(int(input())):
    s = input().lower()
    if s == s[::-1]:
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))

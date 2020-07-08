for i in range(int(input())):
    a, b, c = map(int, input().split())
    max_val = max(a, b, c)
    if max_val >= a + b + c - max_val:
        s = "invalid!"
    elif a == b == c:
        s = "equilateral"
    elif a == b or b == c or a == c:
        s = "isosceles"
    else:
        s = "scalene"
    print("Case #%d: %s" % (i + 1, s))

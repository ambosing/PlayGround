for _ in range(int(input())):
    num, unit = input().split()
    if unit == "kg":
        res = 2.2046 * float(num)
        print("%0.4f lb" % res)
    elif unit == "lb":
        res = 0.4536 * float(num)
        print("%0.4f kg" % res)
    elif unit == "l":
        res = 0.2642 * float(num)
        print("%0.4f g" % res)
    else:
        res = 3.7854 * float(num)
        print("%0.4f l" % res)

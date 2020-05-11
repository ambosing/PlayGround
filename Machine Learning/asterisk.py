def asterisk_test(a, *args):
    print(a, args)
    print(type(args))


def asterisk_test2(a, **kargs):
    print(a, kargs)
    print(type(kargs))


asterisk_test(1, 2, 3, 4, 5, 6)
asterisk_test2(1, b=2, c=3, d=4, e=5, f=6)

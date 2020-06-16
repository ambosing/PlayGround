cnt = 0
while True:
    cnt += 1
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == "E":
        break
    elif op == ">":
        result = a > b
    elif op == ">=":
        result = a >= b
    elif op == "<":
        result = a < b
    elif op == "<=":
        result = a <= b
    elif op == "==":
        result = a == b
    elif op == "!=":
        result = a != b
    if result == True:
        result = "true"
    else:
        result = "false"
    print("Case %d: %s" % (cnt, result))

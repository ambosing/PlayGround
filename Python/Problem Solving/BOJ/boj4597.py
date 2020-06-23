while True:
    s = list(input())
    if s[0] == "#":
        break
    parity = s.pop()
    one_cnt = 0
    zero_cnt = 0
    for c in s:
        if c == "1":
            one_cnt += 1
        if c == "0":
            zero_cnt += 1
    if parity == "e":
        if one_cnt % 2 == 1:
            s.append("1")
        else:
            s.append("0")
    elif parity == "o":
        if one_cnt % 2 == 0:
            s.append("1")
        else:
            s.append("0")
    print(''.join(s))

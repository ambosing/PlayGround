for _ in range(int(input())):
    lst = [0] * 8
    s = input()
    for i in range(len(s) - 2):
        ss = s[i:i + 3]
        if ss == "TTT":
            lst[0] += 1
        elif ss == "TTH":
            lst[1] += 1
        elif ss == "THT":
            lst[2] += 1
        elif ss == "THH":
            lst[3] += 1
        elif ss == "HTT":
            lst[4] += 1
        elif ss == "HTH":
            lst[5] += 1
        elif ss == "HHT":
            lst[6] += 1
        elif ss == "HHH":
            lst[7] += 1
    for i, v in enumerate(lst):
        if i == 7:
            print(v)
        else:
            print(v, end=" ")

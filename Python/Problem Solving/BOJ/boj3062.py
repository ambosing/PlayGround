for _ in range(int(input())):
    s = input()
    num = str(int(s) + int(s[::-1]))
    len_num = len(num)
    chk = True

    for i in range(len_num):
        if num[i] != num[len_num - 1 - i]:
            chk = False
            break
    if chk:
        print("YES")
    else:
        print("NO")

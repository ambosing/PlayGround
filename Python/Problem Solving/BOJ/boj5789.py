for _ in range(int(input())):
    s = input()
    len_s = len(s) // 2
    if s[len_s] == s[len_s - 1]:
        print("Do-it")
    else:
        print("Do-it-Not")

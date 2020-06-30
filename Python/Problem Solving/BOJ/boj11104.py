for _ in range(int(input())):
    s = input()
    result = 0
    adder = 1
    for i in range(23, -1, -1):
        if s[i] == "1":
            result += adder
        adder *= 2
    print(result)

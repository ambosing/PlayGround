while True:
    num = int(input())
    if num == 0:
        break
    while num >= 10:
        print(num, end=" ")
        temp = 1
        while num > 0:
            temp *= num % 10
            num //= 10
        num = temp
    print(num)

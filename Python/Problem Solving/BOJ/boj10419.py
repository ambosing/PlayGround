for _ in range(int(input())):
    c_time = int(input())
    t = 0
    while c_time >= t + t ** 2:
        t += 1
    print(t - 1)

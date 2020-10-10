for _ in range(int(input())):
    res = 0
    stat = list(map(int, input().split()))
    for i in range(4):
        stat[i] += stat[i + 4]
    if stat[0] < 1:
        stat[0] = 1
    if stat[1] < 1:
        stat[1] = 1
    if stat[2] < 0:
        stat[2] = 0
    res = stat[0] + 5 * stat[1] + (stat[2] + stat[3]) * 2
    print(res)

const_lst = [[9.2307, 26.7, 1.835],
             [1.84523, 75, 1.348],
             [56.0211, 1.5, 1.05],
             [4.99087, 42.5, 1.81],
             [0.188807, 210, 1.41],
             [15.9803, 3.8, 1.04],
             [0.11193, 254, 1.88]]
for _ in range(int(input())):
    record = list(map(int, input().split()))
    res = 0
    for i in range(7):
        if i == 0 or i == 3 or i == 6:
            res += int(const_lst[i][0] * (const_lst[i][1] - record[i]) ** const_lst[i][2])
        else:
            res += int(const_lst[i][0] * (record[i] - const_lst[i][1]) ** const_lst[i][2])
    print(res)

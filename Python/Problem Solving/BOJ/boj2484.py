n = int(input())
max_price = 0

for i in range(n):
    lst = list(map(int, input().split()))
    max_cnt = 0
    num_lst = [0] * 10
    for item in lst:
        num_lst[item] += 1
    max_cnt = max(num_lst)
    max_idx = num_lst.index(max_cnt)
    if max_cnt == 4:
        price = 50000 + max_idx * 5000
    elif max_cnt == 3:
        price = 10000 + max_idx * 1000
    elif max_cnt == 2:
        cnt = 0
        max_lst = []
        for idx in range(10):
            if num_lst[idx] == 2:
                cnt += 1
                max_lst.append(idx)
        if cnt == 1:
            price = 1000 + max_lst[0] * 100
        else:
            price = 2000 + max_lst[0] * 500 + max_lst[1] * 500
    elif max_cnt == 1:
        for idx in range(10):
            if num_lst[idx] == 1:
                max_idx = idx
        price = max_idx * 100
    if max_price < price:
        max_price = price
print(max_price)

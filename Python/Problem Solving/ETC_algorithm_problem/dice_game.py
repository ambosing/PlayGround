lst = list()

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    max_cnt = 0
    max_val = 0
    for i in range(1, 7):
        cnt = nums.count(i)
        if max_cnt <= cnt:
            max_cnt = cnt
            max_val = i
    if max_cnt == 3:
        lst.append(10000 + max_val * 1000)
    elif max_cnt == 2:
        lst.append(1000 + max_val * 100)
    elif max_cnt == 1:
        lst.append(max_val * 100)
print(max(lst))

lst = list()
idx_lst = list()
max_val = -1
while True:
    n = int(input())
    if n == 0:
        break
    idx_lst.append(n)
    if max_val < n:
        max_val = n

for i in range(1, max_val + 1):
    if i != 1:
        lst.append(lst[i - 2] + i ** 2)
    else:
        lst.append(1)
for i in idx_lst:
    print(lst[i - 1])

limit = 9
lst = []

for i in range(limit):
    num = int(input())
    lst.append(num)

max_num = max(lst)
print(max_num, lst.index(max_num) + 1)

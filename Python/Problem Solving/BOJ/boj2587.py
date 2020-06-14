lst = []

for i in range(5):
    lst.append(int(input()))
lst.sort()
print(sum(lst) // 5, lst[2])

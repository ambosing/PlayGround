numMode = 0
cnt = 0
lst = []

for i in range(10):
    lst.append(int(input()))

for val in lst:
    if cnt < lst.count(val):
        cnt = lst.count(val)
        numMode = val

print(sum(lst) // len(lst))
print(numMode)

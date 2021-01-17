lst = [i for i in range(20) if i % 2 == 0]
target = int(input())
s = 0
e = len(lst) - 1
while s <= e:
    mid = (s + e) // 2
    if lst[mid] == target:
        break
    elif lst[mid] < target:
        s = mid + 1
    else:
        e = mid - 1
print(mid)

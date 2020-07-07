while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break
    max_val = max(lst)
    sum_val = sum(lst) - max_val
    if max_val >= sum_val:
        print("Invalid")
        continue
    if lst[0] == lst[1] and lst[1] == lst[2]:
        print("Equilateral")
        continue
    if lst[0] == lst[1] or lst[1] == lst[2] or lst[0] == lst[2]:
        print("Isosceles")
        continue
    if lst[0] != lst[1] and lst[0] != lst[2] and lst[1] != lst[2]:
        print("Scalene")

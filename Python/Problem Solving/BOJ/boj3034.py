import math

lst = list(map(int, input().split()))
max_size = int(math.sqrt(lst[1] ** 2 + lst[2] ** 2))
for _ in range(lst[0]):
    matches = int(input())
    if matches <= max_size:
        print("DA")
    else:
        print("NE")

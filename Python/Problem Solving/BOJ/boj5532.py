lst = []
for _ in range(5):
    lst.append(int(input()))

korean_day = lst[1] // lst[3]
math_day = lst[2] // lst[4]
if lst[2] % lst[4] != 0:
    math_day += 1
if lst[1] % lst[3] != 0:
    korean_day += 1
result = lst[0] - max(korean_day, math_day)
print(result)

n = int(input())

move = list(input().split())
x, y = (1, 1)
for m in move:
    if 'R' == m and x < n:
        x += 1
    elif 'L' == m and x > 1:
        x -= 1
    elif 'U' == m and y > 1:
        y -= 1
    elif 'D' == m and y < n:
        y += 1

print(y, x)

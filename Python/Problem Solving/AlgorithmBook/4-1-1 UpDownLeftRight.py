n = int(input())
mv = list(input().split())

x = 1
y = 1
for d in mv:
    if d == 'U' and y > 1:
        y -= 1
    elif d == 'D' and y <= n:
        y += 1
    elif d == 'R' and x <= n:
        x += 1
    elif d == 'L' and x > 1:
        x -= 1
print(y, x)

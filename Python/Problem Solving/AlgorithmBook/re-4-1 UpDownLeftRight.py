n = int(input()) - 1
x = 0
y = 0
d = input()
for i in d:
    if i == 'U' and y > 0:
        y -= 1
    elif i == 'D' and y < n:
        y += 1
    elif i == 'R' and x < n:
        x += 1
    elif i == 'L' and x > 0:
        x -= 1
print(y + 1, x + 1)

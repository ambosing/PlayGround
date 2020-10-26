row = 1
col = 1
n = int(input())
for i in range(n):
    if i % 2 == 0:
        row += 1
    else:
        col += 1
print(row * col)

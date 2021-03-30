from string import ascii_lowercase

inp = input()
alpha = list(ascii_lowercase)
x = alpha.index(inp[0])
y = int(inp[1]) - 1
m = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
cnt = 0
for i in m:
    ny = y + i[0]
    nx = x + i[1]
    if 0 <= ny < 8 and 0 <= nx < 8:
        cnt += 1
print(cnt)


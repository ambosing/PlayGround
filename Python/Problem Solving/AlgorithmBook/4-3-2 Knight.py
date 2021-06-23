from string import ascii_lowercase

s = input()
y = ascii_lowercase.index(s[0])
x = int(s[1]) - 1
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
cnt = 0
for move in moves:
    ny = y + move[0]
    nx = x + move[1]
    if 0 <= ny < 8 and 0 <= nx < 8:
        cnt += 1
print(cnt)

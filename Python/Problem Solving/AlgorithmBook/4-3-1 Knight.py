from string import ascii_lowercase


def is_inner(a, b):
    if 0 <= a < 8 and 0 <= b < 8:
        return True
    return False


alpha = list(ascii_lowercase)
inp = list(input())
col = alpha.index(inp[0])
row = int(inp[1]) - 1
cnt = 0
mv = [2, 1]
for i in range(2):
    if is_inner(row - mv[0], col + mv[1]):
        cnt += 1
    if is_inner(row + mv[0], col - mv[1]):
        cnt += 1
    if is_inner(row + mv[0], col + mv[1]):
        cnt += 1
    if is_inner(row - mv[0], col - mv[1]):
        cnt += 1
    mv = mv[::-1]
print(cnt)

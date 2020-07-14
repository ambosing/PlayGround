import sys


def check(lst, x, y, s):
    for i in range(y, y + s):
        for j in range(x, x + s):
            if lst[y][x] != lst[i][j]:
                return False
    return True


def solution(lst, x, y, s):
    if check(lst, x, y, s):
        sys.stdout.write(lst[y][x])
        return
    sys.stdout.write("(")
    s //= 2
    solution(lst, x, y, s)
    solution(lst, x + s, y, s)
    solution(lst, x, y + s, s)
    solution(lst, x + s, y + s, s)
    sys.stdout.write(")")


n = int(input())
image = list()
for _ in range(n):
    image.append(list(input()))
solution(image, 0, 0, n)

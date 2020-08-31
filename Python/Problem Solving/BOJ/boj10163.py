lst = [[0] * 101 for i in range(101)]


def return_paint_size(paper, paint):
    res = 0
    for i in range(101):
        for j in range(101):
            if paper[i][j] == paint:
                res += 1
    return res


def paint_paper(x, y, w, h, paper, paint):
    for i in range(y, y + h):
        for j in range(x, x + w):
            paper[i][j] = paint


def solution():
    paint = 1
    n = int(input())
    for _ in range(n):
        x, y, w, h = map(int, input().split())
        paint_paper(x, y, w, h, lst, paint)
        paint += 1
    paint = 1
    for _ in range(n):
        print(return_paint_size(lst, paint))
        paint += 1


solution()

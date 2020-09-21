def marking_drawing(drawing, x1, y1, x2, y2):
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            drawing[i][j] += 1


def count_drawing(drawing, m):
    cnt = 0
    for i in range(100):
        for j in range(100):
            if drawing[i][j] > m:
                cnt += 1
    return cnt


def solution():
    n, m = map(int, input().split())
    drawing = [[0] * 100 for _ in range(100)]
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        marking_drawing(drawing, x1, y1, x2, y2)
    print(count_drawing(drawing, m))


solution()

def paint_paper(paper, x, y):
    for i in range(y, y + 10):
        for ii in range(x, x + 10):
            paper[i][ii] = 0


def count_black(paper):
    cnt = 0
    for i in paper:
        for ii in i:
            if ii == 0:
                cnt += 1
    print(cnt)


lst = list()

for j in range(100):
    lst.append([1] * 100)
for _ in range(int(input())):
    b, a = map(int, input().split())
    a = 100 - (10 + a)
    paint_paper(lst, b, a)
count_black(lst)

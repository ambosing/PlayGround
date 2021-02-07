from collections import defaultdict


def check(d):
    if len(d) < 9:
        return False
    return True


def solution():
    n = 9
    b = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for j in range(n):
            dic1[b[i][j]] += 1
            dic2[b[j][i]] += 1
        if not check(dic1) or not check(dic2):
            print("NO")
            return

    for i in range(0, n, 3):
        for j in range(0, n, 3):
            dic = defaultdict(int)
            for k in range(i, i + 3):
                for t in range(j, j + 3):
                    dic[b[k][t]] += 1
            if not check(dic):
                print("NO")
                return
    print("YES")


solution()

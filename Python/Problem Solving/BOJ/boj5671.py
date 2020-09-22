from collections import defaultdict


def solution():
    while True:
        try:
            n, m = map(int, input().split())
        except:
            break
        cnt = 0
        for i in range(n, m + 1):
            i = str(i)
            dic = defaultdict(int)
            for j in i:
                dic[j] += 1
            if max(dic.values()) < 2:
                cnt += 1
        print(cnt)


solution()

from collections import deque


def bfs(a):
    global dis, check
    b = deque([s])
    while True:
        d = deque()
        while b:
            c = b.popleft()
            if c == e:
                print(a)
                exit()
            if check[c] == 0:
                dis[c] = a
                check[c] = 1
            else:
                continue
            for i in [1, -1, 5]:
                if 0 < c + i <= m and check[c + i] == 0:
                    d.append(c + i)
        a += 1
        b = d.copy()


s, e = map(int, input().split())
m = max(s, e)
dis = [0] * (m + 1)
check = [0] * (m + 1)
bfs(0)

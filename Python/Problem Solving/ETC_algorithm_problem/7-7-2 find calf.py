def bfs(a, b):
    if a < 0 or a > e:
        return
    for i in go:
        if 0 <= a + i <= e and dis[a + i] > b + 1:
            dis[a + i] = b + 1
            bfs(a + i, b + 1)


s, e = map(int, input().split())
go = [-1, 1, 5]
dis = [int(1e9)] * (e + 1)
bfs(s, 0)
print(dis[e])

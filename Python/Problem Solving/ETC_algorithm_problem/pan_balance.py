def dfs(a, b):
    if a == k:
        if 1 <= b <= s and check[b] == 0:
            lst.append(b)
            check[b] = 1
    else:
        dfs(a + 1, b + w[a])
        dfs(a + 1, b - w[a])
        dfs(a + 1, b)


k = int(input())
w = list(map(int, input().split()))
s = sum(w)
lst = []
check = [0] * (s + 1)
dfs(0, 0)
print(s - len(lst))

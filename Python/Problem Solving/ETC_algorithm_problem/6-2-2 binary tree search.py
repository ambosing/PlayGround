def dfs1(a):
    if a >= len(lst):
        return
    print(lst[a], end=" ")
    dfs1(a * 2)
    dfs1(a * 2 + 1)


def dfs2(a):
    if a >= len(lst):
        return
    dfs2(a * 2)
    print(lst[a], end=" ")
    dfs2(a * 2 + 1)


def dfs3(a):
    if a >= len(lst):
        return
    dfs3(a * 2)
    dfs3(a * 2 + 1)
    print(lst[a], end=" ")


lst = [i for i in range(8)]
dfs1(1)
print()
dfs2(1)
print()
dfs3(1)

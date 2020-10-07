def dfs(n, flag, lst, hap):
    if n < 0 and hap[0] == hap[1]:
        flag[0] = True
    elif n < 0:
        return
    else:
        hap[0] -= lst[n]
        hap[1] += lst[n]
        dfs(n - 1, flag, lst, hap)
        hap[0] += lst[n]
        hap[1] -= lst[n]
        dfs(n - 1, flag, lst, hap)


def solution():
    n = int(input())
    lst = list(map(int, input().split()))
    flag = [False]
    hap = [sum(lst), 0]
    dfs(n - 1, flag, lst, hap)
    if flag[0]:
        print("YES")
    else:
        print("NO")


solution()

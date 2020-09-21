def print_idx(lst):
    for i, v in enumerate(lst):
        if v == 1:
            print(i + 1, end=" ")
    print()


def dfs(lst, t):
    if len(lst) == t:
        print_idx(lst)
    else:
        lst[t] = 1
        dfs(lst, t + 1)
        lst[t] = 0
        dfs(lst, t + 1)


if __name__ == "__main__":
    n = int(input())
    chk = [0] * n
    dfs(chk, 0)
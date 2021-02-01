n, s, r = map(int, input().split())
lst = [0] * (n + 1)
n_lst = list(map(int, input().split()))
p_lst = list(map(int, input().split()))
for i in n_lst:
    lst[i] = -1
for i in p_lst:
    lst[i] = 1


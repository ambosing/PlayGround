
n, s, r = map(int, input().split())
lst = [0] * (n + 2)
n_lst = list(map(int, input().split()))
p_lst = list(map(int, input().split()))

cnt = s
while p_lst:
    a = p_lst.pop()
    
print(cnt)

for i in n_lst:
    lst[i] += -1
for i in p_lst:
    lst[i] += 1
for i in range(1, n + 1):
    if lst[i] == -1:
        if lst[i - 1] == 1:
            lst[i] = 0
            lst[i - 1] = 0
        elif lst[i + 1] == 1:
            lst[i + 1] = 0
            lst[i] = 0
print(lst.count(-1))



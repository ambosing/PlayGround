s_lst = list(input().split())
min_cnt = 51
if len(s_lst[0]) > len(s_lst[1]):
    max_len = len(s_lst[0])
    min_len = len(s_lst[1])
    max_lst = s_lst[0]
    min_lst = s_lst[1]
else:
    max_len = len(s_lst[1])
    min_len = len(s_lst[0])
    max_lst = s_lst[1]
    min_lst = s_lst[0]
for i in range(0, max_len - min_len + 1):
    cnt = 0
    lst = max_lst[i:min_len + i]
    for j in range(min_len):
        if lst[j] != min_lst[j]:
            cnt += 1
    if min_cnt > cnt:
        min_cnt = cnt
print(min_cnt)

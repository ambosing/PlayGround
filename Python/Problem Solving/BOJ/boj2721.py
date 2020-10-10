def tri_process(lst):
    for i, v in enumerate(lst):
        lst[i] = (i + 1) * (i + 2) // 2


def tri_sum(lst, limit):
    res = 0
    for i in range(1, limit + 1):
        res += i * lst[i]
    return res


t = int(input())
inputs = []

for _ in range(t):
    inputs.append(int(input()))

t_lst = [0] * (max(inputs) + 1)
tri_process(t_lst)
for inp in inputs:
    result = tri_sum(t_lst, inp)
    print(result)


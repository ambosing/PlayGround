s = input()
stack = []
stick_cnt = -1
res = 0
pre = ''

for c in s:
    if pre == '(' and c == ')':
        res += stick_cnt
        stick_cnt -= 1
        pre = c
        continue
    if c == ')':
        stick_cnt -= 1
        res += 1
    else:
        stick_cnt += 1
    pre = c
print(res)

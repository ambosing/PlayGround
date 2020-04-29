t = input()
lst = list(input())
a_cnt = 0
b_cnt = 0
for l in lst:
    if l == 'A':
        a_cnt += 1
    elif l == 'B':
        b_cnt += 1

if a_cnt == b_cnt:
    print("Tie")
elif a_cnt > b_cnt:
    print("A")
elif b_cnt > a_cnt:
    print("B")
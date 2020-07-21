a, n = input().split()
a = list(a)
n = int(n)
lst = []
cnt = 0
top = -1
for i in a:
    while cnt < n and top != -1 and lst[top] < i:
        lst.pop()
        top -= 1
        cnt += 1
    lst.append(i)
    top += 1
while cnt < n:
    cnt += 1
    lst.pop()
lst = list(map(str, lst))
print(''.join(lst))

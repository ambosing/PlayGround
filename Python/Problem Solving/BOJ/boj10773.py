import sys

t = int(input())

lst = []
for i in range(t):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)
print(sum(lst))

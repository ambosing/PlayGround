import sys

t = int(input())

min_lst = []
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    distance = (max(lst) - min(lst)) * 2
    min_lst.append(distance)

for i in min_lst:
    print(i)

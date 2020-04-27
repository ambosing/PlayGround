from sys import stdin

t = int(input())

for i in range(t):
    a, b = map(int, stdin.readline().split())
    divide = 2
    small =  b if a > b else a
    big = a if a > b else b
    while small > 0:
        temp = small
        small = big % small
        big = temp
    print(a * b // big)


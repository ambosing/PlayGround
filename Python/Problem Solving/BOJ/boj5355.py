from sys import stdin

t = int(input())

for i in range(t):
    lst = list(stdin.readline().split())
    answer = 0
    for l in lst:
        if l == '@':
            answer *= 3
        elif l == '%':
            answer += 5
        elif l == '#':
            answer -= 7
        else:
            answer = float(l)
    print('%.2f' % answer)
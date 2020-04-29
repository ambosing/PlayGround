from sys import stdin

t = int(input())

for i in range(t):
    line = list(stdin.readline())
    temp = 0
    score = 0
    for l in line:
        if l == "O":
            temp += 1
            score += temp
        else:
            temp = 0
    print(score)

n = int(input())
lst = list(map(int, input().split()))
score = [0] * (n + 1)
cnt = 1
for i in range(n):
    if lst[i] == 1:
        score[i] = cnt
        cnt += 1
    else:
        cnt = 1
print(sum(score))

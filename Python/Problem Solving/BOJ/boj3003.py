lst = [1, 1, 2, 2, 2, 8]
chess = list(map(int, input().split()))

result = []
for i in range(6):
    result.append(str(lst[i] - chess[i]))
print(' '.join(result))

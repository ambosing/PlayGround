a, b = map(int, input().split())
lst = list(map(int, input().split()))
ab = a * b
for i in range(5):
    lst[i] = str(lst[i] - ab)

print(' '.join(lst))
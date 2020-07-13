import sys

n_a, n_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
ab = list(a - b)
ab.sort()
len_ab = len(ab)

print(len_ab)
for i, v in enumerate(ab):
    if i != len_ab - 1:
        sys.stdout.write(str(v) + " ")
    else:
        sys.stdout.write(str(v) + "\n")

n = int(input())
h = list(map(int, input().split()))
m = int(input())

h.sort()
for _ in range(m):
    h[0] += 1
    h[-1] -= 1
    h.sort()
print(h[-1] - h[0])
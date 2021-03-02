from collections import deque

n, k = map(int, input().split())
q = [i for i in range(1, n + 1)]
q = deque(q)
i = 0
last = 0
while q:
    i += 1
    a = q.popleft()
    if i < k:
        q.append(a)
    else:
        i = 0
    last = a
print(last)

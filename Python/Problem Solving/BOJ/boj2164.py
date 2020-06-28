from collections import deque

n = int(input())
deq = deque([i + 1 for i in range(n)])
for i in range(n - 1):
    deq.popleft()
    deq.append(deq.popleft())
print(deq[0])

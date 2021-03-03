from collections import deque

n, m = map(int, input().split())
d = deque(list(map(int, input().split())))
cnt = 0
max_val = max(d)
while True:
    val = d.popleft()
    if max_val == val:
        cnt += 1
        if m == 0:
            break
        max_val = max(d)
    else:
        d.append(val)
        if m == 0:
            m = len(d)
    m -= 1
print(cnt)

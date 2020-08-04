from collections import deque


def is_more_dangerous(deq):
    for i in deq:
        if deq[0] < i:
            return True
    return False


cnt = 0
n, m = map(int, input().split())
idx = m
lst = list(map(int, input().split()))
deque = deque(lst)
while True:
    val = deque.popleft()
    if is_more_dangerous(deque):
        deque.append(val)
        if idx == 0:
            idx = len(deque)
    else:
        cnt += 1
    if idx == 0:
        break
    idx -= 1
print(cnt)

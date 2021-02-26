from collections import deque

num, m = map(int, input().split())
num = list(str(num))
num = deque(num)
stack = []
while num and m > 0:
    val = num.popleft()
    while stack and stack[-1] < val and m > 0:
        stack.pop()
        m -= 1
    stack.append(val)
for v in num:
    stack.append(v)
while m > 0:
    stack.pop()
    m -= 1
print(''.join(stack))

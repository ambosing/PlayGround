import queue

q = queue.Queue()
n, k = map(int, input().split())
for i in range(1, n + 1):
    q.put(i)
cnt = 0
while q.qsize() > 1:
    cnt += 1
    if cnt == k:
        q.get()
        cnt = 0
    else:
        num = q.get()
        q.put(num)
print(q.get())

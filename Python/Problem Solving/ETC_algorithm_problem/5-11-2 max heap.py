import heapq

h = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (-n, n))

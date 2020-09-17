import heapq

heap = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0 and heap:
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-n, n))

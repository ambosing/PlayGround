import heapq

heap = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0 and heap:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, n)

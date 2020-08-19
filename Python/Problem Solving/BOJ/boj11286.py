import heapq
import sys

heap = []
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    if n == 0:
        if heap:
            sys.stdout.write(str(heapq.heappop(heap)[1]) + "\n")
        else:
            sys.stdout.write("0\n")
    else:
        heapq.heappush(heap, (abs(n), n))

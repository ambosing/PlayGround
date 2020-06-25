import heapq
import sys

heap = []
for _ in range(int(input())):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if heap:
            sys.stdout.write(str(heapq.heappop(heap)) + "\n")
        else:
            sys.stdout.write("0\n")
    else:
        heapq.heappush(heap, num)

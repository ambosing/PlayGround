import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    chk = False
    len_s = len(scoville)
    for i in scoville:
        heapq.heappush(heap, i)
    while heap[0] < K:
        a = heapq.heappop(heap)
        len_s -= 2
        if len_s < 0:
            chk = True
            break
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + b * 2)
        len_s += 1
        answer += 1
    if chk:
        return -1
    return answer
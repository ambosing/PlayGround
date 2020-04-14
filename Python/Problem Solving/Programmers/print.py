from queue import PriorityQueue

def solution(priorities, location):
    answer = 0
    start = 0
    prior_len = len(priorities)
    idx = -1
    for i in range(9, 0, -1):
        start = (idx + 1) % prior_len
        for j in range(prior_len):
            if priorities[start] == i:
                idx = start
                answer += 1
            if priorities[location] == i and start == location:
                break
            start = (start + 1) % prior_len
        if priorities[location] == i and start == location:
            break
    return answer

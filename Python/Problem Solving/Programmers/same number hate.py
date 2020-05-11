def solution(arr):
    answer = []
    pre = None
    for i in arr:
        if i != pre:
            answer.append(i)
        pre = i
    return answer

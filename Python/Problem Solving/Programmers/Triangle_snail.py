def solution(n):
    answer = [0] * (n * (n + 1) // 2)
    idx = 0
    cnt = 1
    s = 0
    for i in range(n):
        for j in range(n - i):
            if i % 3 == 0:
                idx += s + j
            elif i % 3 == 1:
                idx += 1
            else:
                idx -= n - j - i // 3
            answer[idx] = cnt
            cnt += 1
        if i % 3 == 0:
            s += 2
    return answer
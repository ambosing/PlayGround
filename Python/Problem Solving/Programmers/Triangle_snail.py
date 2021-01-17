def solution(n):
    answer = [0] * (n * (n + 1) // 2)
    idx = 0
    cnt = 1
    m = 0
    for i in range(n):
        if i % 3 == 0:
            for j in range(n - i):
                idx += m + j
                answer[idx] = cnt
                cnt += 1
            m += 2
        elif i % 3 == 1:
            for j in range(n - i):
                idx += 1
                answer[idx] = cnt
                cnt += 1
        else:
            for j in range(n - i):
                idx -= n - j - i // 3
                answer[idx] = cnt
                cnt += 1
    return answer
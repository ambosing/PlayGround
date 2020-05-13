def solution(N, stages):
    answer = []
    len_stages = len(stages)
    div = len_stages
    temp_ans = []
    for idx in range(1, N + 1):
        cnt = 0
        for i in range(len_stages):
            if idx == stages[i]:
                cnt += 1
        if div == 0:
            val = 0
        else:
            val = cnt / div
        temp_ans.append([idx, val])
        div -= cnt
    temp_ans = sorted(temp_ans, key=lambda x: x[1], reverse=True)
    for i in range(N):
        answer.append(temp_ans[i][0])
    return answer

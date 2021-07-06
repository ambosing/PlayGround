def solution(s):
    answer = int(1e9)
    for step in range(1, len(s) // 2 + 1):
        ss = ""
        prev = s[0:step]
        cnt = 1
        for i in range(step, len(s), step):
            if prev == s[i:i + step]:
                cnt += 1
            else:
                ss += str(cnt) + prev if cnt > 1 else prev
                cnt = 1
                prev = s[i:i + step]
        else:
            ss += str(cnt) + prev if cnt > 1 else prev
        answer = min(len(ss), answer)
    if len(s) == 1:
        answer = 1
    return answer

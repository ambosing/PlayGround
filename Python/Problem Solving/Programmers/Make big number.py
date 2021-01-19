def solution(number, k):
    answer = ""
    ans_len = len(number) - k
    s = 0
    e = len(number) - ans_len + 1
    for i in range(ans_len):
        p = s
        if number[p] != "9":
            for j in range(s + 1, e):
                if number[j] > number[p]:
                    p = j
                    if number[j] == "9":
                        break
        answer += number[p]
        s = p + 1
        e += 1
    return answer
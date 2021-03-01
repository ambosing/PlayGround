def solution(food_times, k):
    answer = 0
    a = 0
    if sum(food_times) <= k:
        return -1
    for v in food_times:
        if v != 0:
            a += 1
    while k >= a:
        m = k // a
        k -= m * a
        for i, v in enumerate(food_times):
            val = v - m
            if val <= 0 and v != 0:
                k += -val
                food_times[i] = 0
                a -= 1
            elif val > 0:
                food_times[i] = val
    for i, v in enumerate(food_times):
        if k == 0 and v > 0:
            answer = i + 1
            break
        if v > 0:
            k -= 1
    return answer
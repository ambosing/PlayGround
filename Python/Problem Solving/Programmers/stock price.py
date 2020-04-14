def solution(prices):
    answer = []
    leng = len(prices)
    max_price = max(prices)
    j = 0
    for i in range(leng):
        for j in range(i, leng):
            if prices[j] < prices[i]:
                break
        answer.append(j - i)
    return answer

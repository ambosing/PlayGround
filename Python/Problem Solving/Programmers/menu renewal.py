from collections import defaultdict


def dfs(a, b, c, dic, order):
    if len(b) == c:
        b = "".join(sorted(b))
        dic[b] += 1
        return
    for i in range(a, len(order)):
        dfs(i + 1, b + order[i], c, dic, order)


def solution(orders, course):
    answer = []
    for c in course:
        dic = defaultdict(int)
        for order in orders:
            dfs(0, "", c, dic, order)
        if not dic:
            continue
        max_val = max(dic.values())
        for k, v in dic.items():
            if v == max_val and v >= 2:
                answer.append(k)
    answer.sort()
    return answer
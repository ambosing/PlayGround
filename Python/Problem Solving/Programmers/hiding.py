from collections import Counter
from functools import reduce


def solution(clothes):
    cnt = Counter([k for c, k in clothes])
    answer = reduce(lambda a, b: a * (b + 1), cnt.values(), 1)
    return answer - 1


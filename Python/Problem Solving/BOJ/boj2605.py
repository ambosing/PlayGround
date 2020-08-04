def numbering(n, lst):
    result = []
    for i in range(1, n + 1):
        idx = i - lst[i - 1] - 1
        result.insert(idx, str(i))
    return result


def solution():
    n = int(input())
    lst = list(map(int, input().split()))
    result = numbering(n, lst)
    print(' '.join(result))


solution()

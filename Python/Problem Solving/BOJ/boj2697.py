from collections import deque


def find_swap_idx(a, idx):
    min_val = 10
    min_idx = -1
    for i in range(idx, len(a)):
        val = int(a[i]) - int(a[idx - 1])
        if min_val > val and a[idx - 1] < a[i]:
            min_idx = i
            min_val = val
    return min_idx


def solution():
    for _ in range(int(input())):
        a = deque(input())
        idx = len(a) - 1
        while idx > 0:
            if a[idx - 1] < a[idx]:
                break
            idx -= 1
        if idx == 0:
            print("BIGGEST")
        else:
            swap_idx = find_swap_idx(a, idx)
            a[idx - 1], a[swap_idx] = a[swap_idx], a[idx - 1]
            b = []
            for i in range(idx, len(a)):
                b.append(a.pop())
            b.sort()
            a.extend(b)
            print(''.join(a))


solution()

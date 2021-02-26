n = int(input())
nums = list(map(int, input().split()))
lst = [101] * n
for i, v in enumerate(nums):
    i += 1
    for j in range(n):
        if v <= 0 and lst[j] == 101:
            lst[j] = i
            break
        if lst[j] > i:
            v -= 1
lst = list(map(str, lst))
print(' '.join(lst))

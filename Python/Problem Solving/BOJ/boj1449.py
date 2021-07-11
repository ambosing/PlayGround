# L인 테이프, 좌우 0.5만큼 간격
# L - 1 == 간격

# 1. 왼쪽 부터 L - 1 >= 간격
# 2. L - 1 < 간격 -> cnt + 1
# 3. 오른쪽


def solution(arr):
    cnt = 1
    for i, v in enumerate(arr):
        if i == 0:
            a = 0
        else:
            if v > arr[i - 1]:
                a += v - arr[i - 1]
            else:
                a += arr[i - 1] - v
            if a > L - 1:
                cnt += 1
                a = 0
    return cnt


N, L = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
print(min(solution(lst), solution(lst[::-1])))

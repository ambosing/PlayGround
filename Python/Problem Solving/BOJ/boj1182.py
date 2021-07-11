# N개의 정수로 이루어진 수열, 크기가 양수인 부분수열 중 수열을 다 더한 값이 S가 되는 경우의 수를 구하라
# N, S

# 풀이
# 1. 부분 수열 1 ~ N 까지의 수열의 합 경우의 수를 모두 구한다.
# 2. 그 중 S와 같은 것이 있다면 결과값에 +1


def dfs(a, hap):
    global cnt
    if a == n:
        if hap == s:
            cnt += 1
    else:
        dfs(a + 1, hap + arr[a])
        dfs(a + 1, hap)


n, s = map(int, input().split())
cnt = 0
arr = list(map(int, input().split()))
v = [0] * n
dfs(0, 0)
if s == 0:
    cnt -= 1
print(cnt)

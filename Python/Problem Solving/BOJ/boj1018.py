# MN개의 단위 정사각형 M * N 크기의 보드
# 어떤 사각형 -> 검은색, 흰색
# 이 보드를 잘라 8 * 8
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
# 맨 왼쪽 위 칸이 흰색인 경우, 검은색인 경우
# ------------------------------------
# 1. M X N 을 8 x 8로 분할 (2 중 for 문)
# 2. 체스판인지 구하기 (2가지 방법 -> 맨 왼쪽 위가 흰, 검)
# 3. 바꿔야 하는 개수 구하기
# 4. 가장 최소로 하는 개수 구하기


# 2. 체스판인지 구하기
def check(b):
    cnt_b = 0
    cnt_w = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and b[i][j] == 'B':
                # 2.1 흰색
                cnt_w += 1
            elif (i + j) % 2 == 1 and b[i][j] == 'W':
                # 2.1 흰색
                cnt_w += 1
            elif (i + j) % 2 == 0 and b[i][j] == 'W':
                # 2.2 검은색
                cnt_b += 1
            elif (i + j) % 2 == 1 and b[i][j] == 'B':
                # 2.2 검은색
                cnt_b += 1
    return min(cnt_b, cnt_w)


def solution():
    answer = int(1e9)
    m, n = map(int, input().split())
    bb = [list(list(input())) for _ in range(m)]
    for i in range(m - 7):
        for j in range(n - 7):
            # 1. M * N을 8 * 8로 분할
            b = [[bb[r][c] for r in range(i, i + 8)] for c in range(j, j + 8)]
            cnt = check(b)
            answer = min(answer, cnt)
    return answer


print(solution())


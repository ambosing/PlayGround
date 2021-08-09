# 사과를 먹으면 뱀 길이가 늘어남
# 벽 또는 자기 자신의 몸과 부딪히면 게임 오버
# N x N 정사각형 보드
# 사과 존재 -> 그 칸에 있는 사과 제거, 꼬리 움직이지 않는다.
# 사과 존재 X -> 몸길이를 줄여서 꼬리가 위치한 칸을 비운다.
# 뱀은 맨위 좌측 위

# 풀이
# 1. 뱀의 위치를 새로운 2차원 배열에 표기
# 표기할 때 진행했던 방향으로 표기하기
# 2. 방향을 바꿨을 때 뱀의 위치를 표기하는 변수도 변경
# 사과를 먹었을 때 진행방향으로 변수 2차원 배열에 표기
# 3. 이동할 때 시간 모두 세기


def directions_check(ds, dire, sec):
    if ds:
        if sec == int(ds[0][0]):
            if ds[0][1] == 'D':
                dire = dd[(dd.index(dire) + 1) % 4]
            else:
                dire = dd[(dd.index(dire) - 1) % 4]
    return ds, dire


n = int(input())
apples = [tuple(map(int, input().split())) for _ in range(int(input()))]
directions = [tuple(input().split()) for _ in range(int(input()))]
snake = [[0] * n for _ in range(n)]
hx, hy = 0, 0
tx, ty = 0, 0
d = 'R'
dd = ['U', 'R', 'D', 'L']
snake[hy][hx] = d
dic = {'R': (0, 1),
       'L': (0, -1),
       'U': (-1, 0),
       'D': (1, 0)}
cnt = 0
while True:
    cnt += 1
    hx, hy = hx + dic[d][1], hy + dic[d][0]
    if hx < 0 or hx >= n or hy < 0 or hy >= n or snake[hy][hx] != 0:
        break
    for ay, ax in apples:
        if hx == ax - 1 and hy == ay - 1:
            snake[hy][hx] = d
            break
    else:
        snake[hy][hx] = d
        td = snake[ty][tx]
        snake[ty][tx] = 0
        tx, ty = tx + dic[td][1], ty + dic[td][0]
    directions, d = directions_check(directions, d, cnt)
    if d != snake[hy][hx]:
        snake[hy][hx] = d

print(cnt)



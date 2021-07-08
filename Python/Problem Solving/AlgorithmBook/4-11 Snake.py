def solution():
    n = int(input())
    k = int(input())
    apples = [tuple(map(int, input().split())) for _ in range(k)]
    l = int(input())
    directions = [tuple(input().split()) for _ in range(l)]
    d = 'R'

    # 뱀의 길이 표현 방법..
    # 어떻게 해야할까.. 꼬리, 머리 진행방향 표시
    # 꼬리의 진행방향에 벽이나, 0일 경우는 상하좌우를 보고 1인 곳으로만 가면 될까?
    # 

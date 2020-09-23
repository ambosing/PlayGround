def cal_distance(box, x, y):
    all_dist = 0
    for i in range(x):
        dist = 0
        for j in range(y - 1, -1, -1):
            if box[j][i] == 1:
                all_dist += dist
            else:
                dist += 1
    return all_dist


def solution():
    for _ in range(int(input())):
        y, x = map(int, input().split())
        box = []
        for _ in range(y):
            line = list(map(int, input().split()))
            box.append(line)
        print(cal_distance(box, x, y))


solution()

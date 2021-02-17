x, y, w, s = map(int, input().split())
if s < 2 * w:
    cost = min(x, y) * s
    diff = max(x, y) - min(x, y)
    if diff * s < diff * w:
        if diff % 2 == 0:
            cost += diff * s
        else:
            cost += (diff - 1) * s
            cost += w
    else:
        cost += w * diff
else:
    cost = (x + y) * w
print(cost)

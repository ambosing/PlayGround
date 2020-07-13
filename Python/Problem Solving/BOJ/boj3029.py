times = list()
times.append(list(map(int, input().split(":"))))
times.append(list(map(int, input().split(":"))))

s = times[1][2] - times[0][2]
m = times[1][1] - times[0][1]
h = times[1][0] - times[0][0]

if s < 0:
    s += 60
    m -= 1
if m < 0:
    m += 60
    h -= 1
if h < 0:
    h += 24
if h == 0 and m == 0 and s == 0:
    h = 24
print("%0.2d:%0.2d:%0.2d" % (h, m, s))

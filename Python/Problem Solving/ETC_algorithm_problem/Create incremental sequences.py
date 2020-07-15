n = int(input())
arr = list(map(int, input().split()))

s = 0
e = n - 1
if arr[s] < arr[e]:
    num = arr[0]
    idx = s
    s += 1
    res = "L"
else:
    num = arr[e]
    idx = e
    e -= 1
    res = "R"
cnt = 1
for _ in range(n - 1):
    if num < arr[s] < arr[e]:
        num = arr[s]
        s += 1
        res += "L"
    elif num < arr[e] < arr[s]:
        num = arr[e]
        e -= 1
        res += "R"
    else:
        if num < arr[s]:
            num = arr[s]
            s += 1
            res += "L"
        elif num < arr[e]:
            num = arr[e]
            e -= 1
            res += "R"
        else:
            break
    cnt += 1
print(cnt)
print(res)

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for target in b:
    s = 0
    e = n - 1
    while True:
        mid = (s + e) // 2
        if target == a[mid]:
            print('yes', end=" ")
            break
        elif target > a[mid]:
            s = mid + 1
        else:
            e = mid - 1
        if s > e:
            print('no', end=" ")
            break

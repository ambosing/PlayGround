n = int(input())
lst = list(map(int, input().split()))

for i in range(n - 1):
    a, b = lst[0], lst[i + 1]
    while b > 0:
        temp = b
        b = a % b
        a = temp
    print("%d/%d" % (lst[0] // a, lst[i + 1] // a))

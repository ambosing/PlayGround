def count_zero(start, end):
    cnt = 0
    for val in range(start, end + 1):
        s = str(val)
        lst = list(s)
        cnt += lst.count('0')
    return cnt


t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = 0
    result += count_zero(a, b)
    print(result)

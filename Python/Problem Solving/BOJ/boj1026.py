n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse=True)
b.sort()
hap = 0
for i in range(len(a)):
    hap += a[i] * b[i]
print(hap)

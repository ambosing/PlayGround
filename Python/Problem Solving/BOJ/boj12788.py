n = int(input())
m, k = map(int, input().split())
mk = m * k
a = list(map(int, input().split()))
a.sort(reverse=True)
cnt = 0
hap = 0
for i, v in enumerate(a):
    hap += v
    cnt += 1
    if mk <= hap:
        print(cnt)
        break
else:
    print("STRESS")


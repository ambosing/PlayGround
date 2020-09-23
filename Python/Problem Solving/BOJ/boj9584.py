s = input().split()
s = ''.join(s)
cnt = 0
res = []

for _ in range(int(input())):
    s2 = input()
    for i, c in enumerate(s):
        if c == "*":
            continue
        elif c != s2[i]:
            break
    else:
        cnt += 1
        res.append(s2)
print(cnt)
for line in res:
    print(line)

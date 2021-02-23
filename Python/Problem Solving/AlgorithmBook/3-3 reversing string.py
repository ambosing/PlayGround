s = input()
cnt1 = 0
cnt2 = 0
for i in range(1, len(s)):
    if (i == 0 or s[i - 1] == '1') and s[i] == '0':
        cnt1 += 1
    elif (i == 0 or s[i - 1] == '0') and s[i] == '1':
        cnt2 += 1
print(min(cnt1, cnt2))

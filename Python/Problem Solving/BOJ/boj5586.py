s = input()
joi_cnt = 0
ioi_cnt = 0
len_s = len(s) - 2
for i in range(len_s):
    temp = s[i:i + 3]
    if temp == "JOI":
        joi_cnt += 1
    elif temp == "IOI":
        ioi_cnt += 1

print(joi_cnt)
print(ioi_cnt)

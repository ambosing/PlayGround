s = input()
s = sorted(s)
idx = 0
while s[idx].isdigit():
    idx += 1
nums = list(map(int, s[:idx]))
alpha = s[idx:]
print(''.join(alpha) + str(sum(nums)))

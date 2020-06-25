target = input()
result = 0
target_len = len(target)

for _ in range(int(input())):
    s = input()
    if s.count(target) >= 1:
        result += 1
    else:
        for i in range(11 - target_len, 10):
            ss = []
            for j in range(i, i + target_len):
                ss.append(s[j % 10])
            ss = ''.join(ss)
            if target.count(ss):
                result += 1
                break
print(result)

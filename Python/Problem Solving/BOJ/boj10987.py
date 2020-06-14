s = input()
cnt = 0
vowel = ['a', 'e', 'i', 'o', 'u']

for i in s:
    if i in vowel:
        cnt += 1

print(cnt)

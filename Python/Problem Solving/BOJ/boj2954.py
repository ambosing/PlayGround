s = list(input())

for i, v in enumerate(s):
    if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
        s.pop(i + 1)
        s.pop(i + 1)
print(''.join(s))

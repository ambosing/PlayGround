vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input()
    if s[0] == "#":
        break
    res = str()
    if s[0] in vowel:
        print(s + "ay")
        continue
    only_consonant_chk = True
    for i, c in enumerate(s):
        if c in vowel:
            only_consonant_chk = False
            idx = i
            break
    if only_consonant_chk:
        print(s + "ay")
    else:
        print(s[idx:] + s[:idx] + "ay")

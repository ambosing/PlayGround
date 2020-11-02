from collections import defaultdict
from sys import stdout


t = int(input())

for ii in range(t):
    s1, s2 = input().split()
    if len(s1) != len(s2):
        stdout.write(s1 + " & " + s2 + " are NOT anagrams.\n")
        continue
    dic1, dic2 = defaultdict(int), defaultdict(int)
    for i, j in zip(s1, s2):
        print(i, j)
        dic1[i] += 1
        dic2[j] += 1
    for k1, k2 in zip(dic1.keys(), dic2.keys()):
        if dic1[k1] != dic2[k1] or dic1[k2] != dic2[k2]:
            stdout.write(s1 + " & " + s2 + " are NOT anagrams.")
            break
    else:
        stdout.write(s1 + " & " + s2 + " are anagrams.")
    if ii != t - 1:
        stdout.write("\n")

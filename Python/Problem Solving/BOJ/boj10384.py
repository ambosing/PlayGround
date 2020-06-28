import string
import sys


for i in range(int(input())):
    alpha_low = dict.fromkeys(list(string.ascii_lowercase), 0)
    chk = [True] * 3
    s = sys.stdin.readline().rstrip().lower()
    for c in s:
        if c.islower():
            alpha_low[c] += 1
    min_val = min(alpha_low.values())
    if min_val == 1:
        sys.stdout.write("Case " + str(i + 1) + ": " + "Pangram!\n")
    elif min_val == 2:
        sys.stdout.write("Case " + str(i + 1) + ": " + "Double pangram!!\n")
    elif min_val == 3:
        sys.stdout.write("Case " + str(i + 1) + ": " + "Triple pangram!!!\n")
    else:
        sys.stdout.write("Case " + str(i + 1) + ": " + "Not a pangram\n")


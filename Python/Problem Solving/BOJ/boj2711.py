import sys

num = int(input())

for i in range(num):
    idx, sentence = sys.stdin.readline().rstrip().split()
    sentence = list(sentence)
    idx = int(idx) - 1
    sentence.pop(idx)
    sentence = ''.join(sentence)
    sys.stdout.write(sentence + "\n")

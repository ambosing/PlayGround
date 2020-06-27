answer = [((j - 1) % 5) + 1 for j in range(1, 11)]

for i in range(int(input())):
    std_answer = list(map(int, input().split()))
    chk = True
    for j in range(10):
        if answer[j] != std_answer[j]:
            chk = False
    if chk:
        print(i + 1)

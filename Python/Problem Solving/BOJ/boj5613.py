lst = []
cnt = 0
while True:
    s = input()
    if s == "=":
        break
    lst.append(s)
    cnt += 1
    if cnt == 3:
        if lst[1] == "+":
            result = int(lst[0]) + int(lst[2])
        elif lst[1] == '-':
            result = int(lst[0]) - int(lst[2])
        elif lst[1] == '*':
            result = int(lst[0]) * int(lst[2])
        elif lst[1] == '/':
            result = int(lst[0]) / int(lst[2])
        lst = [result]
        cnt = 1
print(lst[0])
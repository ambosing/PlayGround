from sys import stdout


n = int(input())
for _ in range(n):
    m = int(input())
    i = 2
    cnt = 0
    while m > 1:
        if m % i == 0:
            m //= i
            cnt += 1
        else:
            if cnt > 0:
                stdout.write(str(i) + " " + str(cnt) + "\n")
            i += 1
            cnt = 0
    stdout.write(str(i) + " " + str(cnt) + "\n")


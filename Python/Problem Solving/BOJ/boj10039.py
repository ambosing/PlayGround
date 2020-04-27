hap = 0
for i in range(5):
    l = int(input())
    if l < 40:
       hap += 40
    else:
        hap += l

print(hap // 5)

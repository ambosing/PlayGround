a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_score = 0
b_score = 0
last = str()
for i in range(10):
    if a[i] > b[i]:
        a_score += 3
        last = 'A'
    elif a[i] < b[i]:
        b_score += 3
        last = 'B'
    else:
        a_score += 1
        b_score += 1

print(a_score, b_score)
if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
else:
    if last == 'A':
        print('A')
    elif last == 'B':
        print('B')
    else:
        print('D')

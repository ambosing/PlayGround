lst_w = []
lst_k = []

for i in range(10):
    num = int(input())
    lst_w.append(num)
lst_w.sort(reverse=True)
for i in range(10):
    num = int(input())
    lst_k.append(num)
lst_k.sort(reverse=True)
sum_w = lst_w[0] + lst_w[1] + lst_w[2]
sum_k = lst_k[0] + lst_k[1] + lst_k[2]
print(sum_w, sum_k)

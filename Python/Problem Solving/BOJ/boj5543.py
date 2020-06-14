import sys

lst = []

for i in range(5):
    lst.append(int(input()))

minPrice = sys.maxsize
result = []
for i in range(3):
    price1 = lst[i] + lst[3] - 50
    price2 = lst[i] + lst[4] - 50
    minPrice = min(minPrice, price1, price2)
print(minPrice)

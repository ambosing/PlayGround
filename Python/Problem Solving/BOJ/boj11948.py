lst1 = []
lst2 = []
for i in range(6):
	if i < 4:
		lst1.append(int(input()))
	else:
		lst2.append(int(input()))
lst1.sort()
lst2.sort()
res = sum(lst1) + sum(lst2) - (lst1[0] + lst2[0])
print(res)

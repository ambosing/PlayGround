s = input()
lst = list(s)

lst.sort(reverse=True)
s = ''.join(lst)
print(s)

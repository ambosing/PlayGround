for i, v in enumerate(['t', 'a', 'e']):
    print(i, v)

mylist = ['a', 'b', 'c', 'd']
print(list(enumerate(mylist)))

print({i:j for i, j in enumerate('g u i a ac in')})


alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)
print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])

n = int(input())
lst = [int(input()) for _ in range(n)]

lst.sort(reverse=True)
lst = map(str, lst)
print(' '.join(lst))

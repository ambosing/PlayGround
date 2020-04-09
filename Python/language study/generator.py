def number_generator():
    yield 0
    yield 1
    yield 2

for i in number_generator():
    print(i)

def file_read():
    with open('words.txt') as file:
        lines = file.read().split('\n')
        for line in lines:
            yield line

for i in file_read():
    print(i)

def prime_number_generator(start, stop):
    i = start
    while i < stop:
        j = 2
        while j < i:
            if i % j == 0:
                break
            j += 1
        if i == j:
            yield i
        i += 1

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
def number_coroutine():
     while True:
         x = (yield)
         print(x)

co = number_coroutine()
next(co)

co.send(1)
co.send(2)
co.send(3)

def find(word):
    result = False
    while True:
        line = (yield result)
        result = word in line

f = find('Python')
next(f)

print(f.send('Hello, Python!'))
print(f.send('Hello, world!'))
print(f.send('Python Script'))

f.close()

def calc():
    result = list()
    while True:
        lst_cal = (yield result)
        lst_oper = lst_cal.split()
        if lst_oper[1] == '+':
            result = int(lst_oper[0]) + int(lst_oper[2])
        elif lst_oper[1] == '-':
            result = int(lst_oper[0]) - int(lst_oper[2])
        elif lst_oper[1] == '/':
            result = int(lst_oper[0]) / int(lst_oper[2])
        elif lst_oper[1] == '*':
            result = int(lst_oper[0]) * int(lst_oper[2])

expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()
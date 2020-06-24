def operator_add(res, operator_):
    op = operator_.pop()
    res.append(op)


def mul_div(item, res, operator_):
    if item == '*' or item == '/':
        while operator_ and (operator_[-1] == '*' or operator_[-1] == '/'):
            operator_add(res, operator_)
        operator_.append(i)


def plus_minus(item, res, operator_):
    if item == '+' or item == '-':
        while operator_ and \
                (operator_[-1] == '+' or operator_[-1] == '-' or operator_[-1] == '*' or operator_[-1] == '/'):
            operator_add(res, operator_)
        operator_.append(i)


def bracket(item, res, operator_):
    if item == '(':
        operator.append(i)
    elif item == ')':
        while operator_ and operator_[-1] != '(':
            operator_add(res, operator_)
        operator_.pop()


lst = list(input())
result = []
operator = []

for i in lst:
    if i.isalpha():
        result.append(i)
    mul_div(i, result, operator)
    plus_minus(i, result, operator)
    bracket(i, result, operator)
while operator:
    operator_add(result, operator)
print(''.join(result))

def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

def print_numbers_args(*args):
    for arg in args:
        print(arg)

def print_args(a, *args):
    print(a)
    print(args)

def personal_info(name, age, address):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

def personal_info_args(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

def personal_info2(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

x = [10, 20, 30]
print_numbers(10, 20, 30)
print_numbers(*x)
print_numbers(*[10, 20, 30])

print_numbers_args(10)
print_numbers_args(10, 20, 30, 40)

print_args(1)
print_args(1, 10, 20)
print_args(*[10, 20, 30])

personal_info('홍길동', 30, '서울시 용산구 이촌동')
personal_info(name = '홍길동', age = 30, address = '서울시 용산구 이촌동')

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
personal_info2(**x)

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return (min(args), max(args))
def get_average(**args):
    sum_val = 0
    count = 0
    for key, value in args.items():
        sum_val += value
        count += 1
    return (sum_val / count)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))


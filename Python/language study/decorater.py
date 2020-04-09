def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper():  # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')

    return wrapper  # wrapper 함수 반환

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')


hello()
world()


def decorator1(func):
    def wrapper():
        print('decorator1')
        func()

    return wrapper


def decorator2(func):
    def wrapper():
        print('decorator2')
        func()

    return wrapper


# 데코레이터를 여러 개 지정
@decorator1
@decorator2
def hello():
    print('hello')


hello()

def html_tag(x):
    def real_decorator(func):
        def wrapper():
            res = '<' + x + '>' + func() + '</' + x + '>'
            return res
        return wrapper
    return real_decorator

a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

print(hello())

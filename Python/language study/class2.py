class Person:
    '''사람 클래스입니다.'''
    bag = []

    def put_bag(self, stuff):
        '''가방 메서드입니다.'''
        Person.bag.append(stuff)


class Person2:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)


class Person3:
    count = 0  # 클래스 속성

    def __init__(self):
        Person3.count += 1  # 인스턴스가 만들어질 때
                           # 클래스 속성 count에 1을 더함
    @classmethod
    def create(cls):
        p = cls()
        return p

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(Person3.count))

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(Person.__doc__)
print(Person.put_bag.__doc__)
print(james.bag)
print(maria.bag)

james = Person2()
james.put_bag('책')

maria = Person2()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

qwe = Person3()
wer = Person3()

Person3.print_count()

aa = Person3.create()
Person3.print_count()

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        p = cls(hour, minute, second)
        return p

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        if hour <= 23 and minute <= 59 and second <= 60:
            return True
        else:
            False


time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
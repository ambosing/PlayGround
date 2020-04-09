class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hello'

    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()
        self.school = 'python coding school'

    def study(self):
        print('공부하기')


class Person2:
    def greeting(self):
        print('안녕하세요.')


class PersonList:
    def __init__(self):
        self.person_list = []  # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person2):  # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person2)

james = Student()
james.greeting()
james.study()

print(issubclass(Student, Person))
print(issubclass(Person, Student))

james = Student()
print(james.school)
print(james.hello)

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교에 간다')

james = Student()
james.study()


class Animal:
    def eat(self):
        print('먹다')

class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal, Wing):
    def fly(self):
        print('날다')

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))

import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

length = 0
for i in range(3):
    a = (p[i].x - p[i + 1].x) ** 2
    b = (p[i].y - p[i + 1].y) ** 2
    length += math.sqrt(a + b)
print(length)
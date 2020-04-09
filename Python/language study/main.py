import square2

print(square2.base)
print(square2.square(10))

from square2 import base, square

print(base)
print(square(10))

from person import Person

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

import hello

if __name__ == '__main__':
    print('main.py __name__:', __name__)
'''
import calcpkg.operation
import calcpkg.geometry

print(calcpkg.operation.add(10, 20))
print(calcpkg.operation.mul(10, 20))

print(calcpkg.geometry.triangle_area(30, 40))
print(calcpkg.geometry.rectangle_area(30, 40))

import calcpkg

print(calcpkg.add(10, 20))
print(calcpkg.mul(10, 20))

print(calcpkg.triangle_area(30, 40))
print(calcpkg.rectangle_area(30, 40))

'''

import calcpkg.operation
import calcpkg.geometry

n = float(input())
print(calcpkg.operation.squareroot(n))
print(calcpkg.geometry.circle_area(n))
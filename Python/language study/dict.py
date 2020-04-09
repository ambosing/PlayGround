from collections import defaultdict
import copy

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
x.setdefault('f', 100)
print(x)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a = 90)
print(x)
# 없는 내용은 키와 밸류가 같이 추가가 된다.
x.update(e = 50)
print(x)
# update는 키가 문자열일 때만 사용할 수 있다.
# y.update(1 = 'ONE') (x)
# y.update({1 : 'ONE', 3: 'THREE'}) (o)

y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
print(y)

y.update([[2, 'TWO'], [4, 'FOUR']])
print(y)

y.update(zip([1, 2], ['one', 'two']))
print(y)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.pop('a'))
print(x)
print(x.pop('z', 0))

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.popitem())
print(x)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
print(x)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('a'), x['a'])
print(x.items())
print(x.keys())
print(x.values())

keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)

y = dict.fromkeys(keys, 100)
print(y)

y = defaultdict(int)
print(y['z'])

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end = ' ')
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key in x.keys():
    print(key, end = ' ')

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for value in x.values():
    print(value, end = ' ')
print()

keys = ['a', 'b', 'c', 'd']
x = {key : value for key, value in dict.fromkeys(keys).items()}
print(x)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key : value for key, value in x.items() if value != 20}
print(x)

terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}

print(terrestrial_planet['Venus']['mean_radius'])

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
print(x is y)
y['a'] = 99
print(x)
print(y)

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy()
print(x is y)
print(x == y)

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()
y['a']['python'] = '3.7.2'
print(x)
print(y)

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = copy.deepcopy(x)
y['a']['python'] = '3.7.2'
print(x)
print(y)

keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x = {key : value for key, value in x.items() if key != 'delta' and value != 30}
print(x)
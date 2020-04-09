class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)

class Annie:
    def __init__(self, **kwargs):
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        self.ability_power = kwargs['ability_power']

    def tibbers(self):
        print("티버: 피해량 %g" % (float(self.ability_power) * 0.65 + 400.0))

health, mana, ability_power = map(float, input().split())

x = Annie(health = health, mana = mana, ability_power = ability_power)
x.tibbers()
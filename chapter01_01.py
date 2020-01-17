#chapter01-01
#파이썬 중급
#객체 지향 프로그래밍(OOP) --> 코드의 재사용, 코드중복 방지
#클래스 사용 장점
#리스트 구조: 관리하기 불편, 인덱스 접근시 실수가능성, 삭제 불편
#딕셔너리 구조: 코드 반복 지속, 중첩문제(key가 중복될수 있음), 삭제불편

car_name_list = ['BMW', 'Ferrari', 'Audi']
car_detail_list = [
    {'horsepower': 600, 'color':'red', 'price':4000},
    {'horsepower': 400, 'color':'black', 'price':1000},
    {'horsepower': 800, 'color':'white', 'price':7000},
]

#del car_name_list.del
#car_name_list.pop(1)

# unmanaged language: 포인터로 할당해야하는 언어: C
# managed language: 코딩 --> 메모리할당 자동: java, python, ruby, rust, golang, javascript

class Car(object):
    pass

class Car():
    pass

class Car:
    pass

class Car(object):
    
    def __init__(self, car_name, car_detail):
        self.car_name = car_name
        self.car_detail = car_detail
        pass
    
    def __str__(self):
        return 'Str: {} - {}'.format(self.car_name, self.car_detail)

    def __repr__(self):
        return 'Repr: {} - {}'.format(self.car_name, self.car_detail)
        
car1 = Car('BMW', {'horsepower': 600, 'color':'red', 'price':4000})
car2 = Car('Ferrari', {'horsepower': 400, 'color':'black', 'price':1000})
car3 = Car('Audi', {'horsepower': 800, 'color':'white', 'price':7000})

#python magic method: 리스트로 되어있음, 이 메소드를 활용하여 패키지를 만든다, 메모리 절약

#ID주소 
print(id(car1))
print(id(car2))
print(id(car3))

#네임스페이스
print(dir(car1)[0])
print(car1.__dict__)

#doc
print(Car.__doc__)

#클래스 원형
print(car1.__class__)

#str메소드
print(car1)

del car1
print(car1)
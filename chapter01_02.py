#chapter01-02
#파이썬 중급
#객체 지향 프로그래밍(OOP) --> 코드의 재사용, 코드중복 방지
#클래스 변수 심화 (final static ...)

#클래스 선언
class Car(object):
    """
    author : taewon
    date : 2020.01.15
    comment : example
    """
    #자동차의 개수
    car_count = 0
    클래스변수=5

    def __init__(self, car_name, car_detail):
        self.car_name = car_name
        self.car_detail = car_detail
        Car.car_count += 1
    
    def __str__(self):
        return 'Str: {} - {} - {}'.format(id(self), self.car_name, self.car_detail)

    def __repr__(self):
        return 'Repr: {} - {} - {}'.format(id(self), self.car_name, self.car_detail)

    def price_info(self):
        return '{} - {}'.format(self.car_name, self.car_detail.get('price'))
        
car1 = Car('BMW', {'horsepower': 600, 'color':'red', 'price':4000})
car2 = Car('Ferrari', {'horsepower': 400, 'color':'black', 'price':1000})
car3 = Car('Audi', {'horsepower': 800, 'color':'white', 'price':7000})

#id값 비교
print(id(car1), car1)

#메소드 호출(self)
print(car2.price_info())

#메소드 호출(class)
print(Car.price_info(car2))

#클래스 변수 출력
print(Car.car_count)

#인스턴스로 클래스 변수 접근 출력
print(car1.car_count)

car1.car_count = 10

#네임스페이스 메소드
print(car1.__dict__)
car1.car_count = 1000
print(car1.car_count*10)

# 인스턴스 네임스페이스를 먼저 검색후 없으면 클래스 변수를 출력
print(car1.클래스변수)
print(Car.클래스변수)

print(Car.__dict__)
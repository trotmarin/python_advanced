#chapter01-03
#파이썬 중급
#객체 지향 프로그래밍(OOP) --> 코드의 재사용, 코드중복 방지
# static method, instance method, class method

#클래스 선언
class Car(object):
    """
    author : taewon
    date : 2020.01.17
    comment : class method example
    """
    #자동차의 개수
    car_count = 0

    #자동차 가격 인상률
    car_price_per = 1.2

    #instance method
    def __init__(self, car_name, car_detail):
        self.car_name = car_name
        self.car_detail = car_detail
        Car.car_count += 1

    #instance method
    def __str__(self):
        return 'Str: {} - {} - {}'.format(id(self), self.car_name, self.car_detail)
        
    #instance method
    def __repr__(self):
        return 'Repr: {} - {} - {}'.format(id(self), self.car_name, self.car_detail)
        
    #instance method
    def price_info_before(self):
        return '{} - {}'.format(self.car_name, self.car_detail.get('price'))

    #instance method:셀프가 누군지 모름, 인스턴스가 없으면 호출할수 없음
    def price_info_after(self):
        return '{} - {}'.format(self.car_name, int(self.car_detail.get('price')* Car.car_price_per))
      
    #instance method
    def __del__(self):
        Car.car_count -= 1

# 클래스변수를 직접접근하지않고 수정할때 사용, 더 객체지향적 코드
    @classmethod
    def set_price_per(cls, p):
        #클래스 원형
        print(cls ==Car)
        print(cls is Car)
        print(cls.__class__ == Car.__class__)
        if p <= 1:
            print('please enter 1 more')
            return
        cls.car_price_per = p

    # @staticmethod
    def is_bmw(self):
        if self.car_name == 'BMW':
            print('succeed Bmw - {}'.format(self.car_detail.get('horsepower')))
        else:
            print("no bmw found")

car1 = Car('BMW', {'horsepower': 600, 'color':'red', 'price':4000})
car2 = Car('Ferrari', {'horsepower': 400, 'color':'black', 'price':1000})
car3 = Car('Audi', {'horsepower': 800, 'color':'white', 'price':7000})

#클래스 변수 확인
print(Car.car_count)

# 인스턴스 소멸
# del car2
# car2.__del__()

#클래스 변수 확인
print(Car.car_count)

#자동차 가격 인상전
print(car1.price_info_before())
print(car2.price_info_before())
print(car3.price_info_before())

#줄바꿈
print('-'*50)

#자동차 가격 인상후
print(car1.price_info_after())
print(car2.price_info_after())
print(car3.price_info_after())

# 클래스 변수 직접 접근 수정이 가능하다(unsafe)
# Car.car_price_per = 0.4

Car.set_price_per(0.5)

# bmw찾기, car class 밖에서 정의
def is_bmw(inst):
    if inst.car_name == 'BMW':
        print('succeed Bmw - {}'.format(inst.car_detail.get('horsepower')))
    else:
        print("no bmw found")

# 전체 자동차 리스트
car_list = [car1, car2, car3]

for inst in car_list:
    is_bmw(inst)

#줄바꿈
print('-'*50)

for inst in car_list:
    Car.is_bmw(inst)
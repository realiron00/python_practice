"""
*초기화 메소드(initialize method): 인스턴스가 생성될 때 자동으로 호출되어 변수를 초기화해주는 메소드

class Dog:
    def setinfo(self, name):
       self.name = name
    def bark(self):
       print(self.name + "가 멍멍하고 짖는다.")

my_dog = Dog()
my_dog.bark()
=>AttributeError가 발생하며 name이라는 이름의 변수가 없다는 에러 메시지를 출력
->bark() 메소드를 호출하기 전, set_info() 메소드가 호출되어 name이라는 변수를 먼저 선언해야 하는 구조

초기화 메소드 이름: __init__

__init__ 메소드는 인스턴스가 생성되는 시점에서 자동으로 호출
"""
class Dog:  #클래스 선언
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + "가 멍멍하고 짖는다")

my_dog = Dog("삼식이")  #인스턴스 생성, 초기화 메소드를 사용하여 속성을 자동으로 초기화
my_dog.bark()  #인스턴스의 메소드 호출
print("-------")

"""
*클래스 변수와 인스턴스 변수

클래스 변수(class variable): 해당 클래스에서 생성된 모든 인스턴스가 값을 공유하는 변수
인스턴스 변수(instance variable): __init__() 메소드 내에서 선언된 변수
                                  인스턴스가 생성될 때마다 새로운 값이 할당되는 변수
"""
class mcu:  #클래스 선언
    hero = "어벤져스"  #클래스 변수 선언

    def __init__(self, name):
        self.name = name  #인스턴스 변수 선언

    def endgame(self):
        print(self.name + "이/가 엔드게임에 출연했다.")

my_mcu = mcu("아이언맨")  #인스턴스 생성
your_mcu = mcu("토르")  #인스턴스 생성

print(my_mcu.hero)  #클래스 변수에 접근
print(my_mcu.name)  #인스턴스 변수에 접근

print(your_mcu.hero)  #클래스 변수에 접근
print(your_mcu.name)  #인스턴스 변수에 접근
'''
인스턴스 간에 값을 서로 공유하지 않아도 되는 변수: 인스턴스 변수로 선언
인스턴스 간에 같은 값을 공유해야만 하는 변수: 클래스 변수로 선언
'''
'''
어떤 변수를 선언해야 할지 모른다면 인스턴스 변수로 선언(프로그램의 안전성)
코드가 중복될 가능성은 생기지만 프로그램이 의도치 않게 동작할 가능성은 줄어듦
'''

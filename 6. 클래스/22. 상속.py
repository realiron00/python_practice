"""
*상속(inheritance): 이미 존재하는 클래스의 특징을 물려받는 것

기존 클래스를 직접 수정하지 않고, 기능을 추가하거나 변경하고 싶을 때 유용하게 사용

부모 클래스(parent class)(=기초 클래스(base class)): 이미 존재하던 클래스
자식 클래스(child class)(=파생 클래스(derived class)): 상속을 통해 새롭게 생성되는 클래스
"""

"""
*클래스 상속하기

소괄호(())를 사용, 그 안에 상속받고 싳은 클래스명을 넣어 전달

문법:
class 자식클래스명(부모클래스명):
"""
class samsung:
    def __init__(self):
        self.company = True

    def galaxy(self):
        print("삼성")

class phone(samsung):  #samsung 클래스를 상속받음
    def galaxy(self):
        print("갤럭시 s20")

my_phone = phone()

print(my_phone.company)  #company 속성을 자유롭게 사용 가능
my_phone.galaxy()
print("-------")

"""
*메소드 오버라이딩(method overriding)

메소드 오버라이딩: 부모 클래스의 메소드를 자식 클래스에서 같은 이름으로 재정의하는 것
                   메소드를 재정의하여 추가하거나 변경
"""
class mcu:
    def __init__(self):
        self.flying = True

    def name(self):
        print("어벤져스")

class tony(mcu):
    def name(self):  #name() 메소드를 재정의
        print("아이언맨")

class steve(mcu):  #name() 메소드를 재정의하지 않음
    def __init__(self):
        self.flying = False

my_tony = tony()
my_steve = steve()

my_tony.name()
my_steve.name()  #부모클래스(mcu)의 name 메소드를 그대로 사용

"""
*접근 제어(access control)

정보 은닉(data hiding)의 원칙: 알 필요가 없는 정보는 되도록 사용자로부터 숨겨야 한다.
                               객체 지향 프로그래밍 언어(자바, C++ 등)에서 사용

접근 제어자(access modifier): 클래스 외부에서의 직접적인 접근을 허용하지 않는 속성이나 메소드 선언 가능
                              정보 은닉과 캡슐화(encapsulation)를 구체화

파이썬에서는 접근제어자를 사용하지 않고도, 변수나 메소드 이름의 작명법(naming)에 때라 접근 제어를 구현

접근 제어자:
1. public: 선언된 클래스 멤버는 외부로 공개, 해당 객체를 사용하는 프로그램 어디에서나 직접 접근 가능
   -파이썬: 멤버 이름에 어떠한 언더스코어(_)도 포함되지 않음(ex. name)
2. private: 선언된 클래스 멤버는 외부로 공개하지 않음, 외부에서는 직접 접근 불가능
   -파이썬: 멤버 이름 앞에 두 개의 언더스코어(__)가 접두사로 포함됨(ex. __name)
3. protected: 선언된 클래스 멤버는 부모클래스에 대해서는 public 멤버, 외부에서는 private 멤버로 취급
   -파이썬: 멤버 이름 앞에 한개의 언더스코어(_)가 접두사로 포함됨(ex. _name)
"""

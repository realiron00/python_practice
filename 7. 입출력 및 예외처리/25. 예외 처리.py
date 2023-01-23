"""
*예외 처리(exception handing)

오류:
1. 문법 오류(syntax errors)
2. 예외(exception): 프로그램을 작성 후 실행하는 중 오류가 발생하여 실행하던 프로그램이 중지되는 것
"""

"""
*try, except 문

예외 처리(exception handing): 예외 상황을 처리할 수 있도록 프로그램의 흐름을 바꾸는 행위
                              try, except 문이라는 예외 처리 구문을 제공

예제:
try:
   예외가 발생할 가능성이 있는 코드
except [ 처리할 예외명 [as 에러 메시지 변수 ]]:
   try 절에서 발생한 예외를 처리할 코드
[ else: ]
   try 절에서 예외가 발생하지 않았을 경우에만 실행될 코드
[ finally: ]
   try 절이 실행되고 나면 언제나 마지막에 실행될 코드

대괄호([]): 해당 구문을 반드시 사용할 필요 없이 생략할 수 있다는 의미
"""

"""
*try, except 문의 동작 순서

1. try 블록에 포함된 코드가 순서대로 실행

2. 예외가 발생하지 않으면, except 절은 실행되지 않고 try, except 문은 그대로 종료

3. 예외가 발생했다면, 곧바로 발생한 예외명과 except 절에 명시한 예외명이 같은지를 순서대로 확인
3-1. 발생한 예외명과 명시된 예외명이 같음 -> 해당 except 절 실행
                                             프로그램의 흐름은 try 문 다음으로 넘어감
3-2. 발생한 예외명과 명시된 예외명이 같지 않음 -> 다음 except 절을 계속해서 확인
3-2-1. 발생한 예외명과 명시된 예외명이 같은 except 절을 찾지 못함 -> try문 바깥쪽의 except 절들 확인
3-2-2. 발생한 예외명과 명시된 예외명이 같은 except 절을 찾을 수 없음 -> 에러 메시지를 출력
                                                                        프로그램은 강제 종료
"""
try:
    3 / 0  #ZeroDivisionError 발생
except IndexError as e:
    print("인덱스가 맞지 않습니다", e)
except ZeroDivisionError as e:
    print("0으로 나누면 안됩니다.", e)

print("프로그램이 정상적으로 종료됩니다.")
print("-------")

"""
*else 절과 finally 절

else 절: try 블록에서 예외가 발생하지 않았을 경우에만 실행됨
         반드시 except 절 바로 다음에 위치
         생략 가능

finally 절: try 블록이 실행되고 나면 예외 발생 여부와 상관없이 언제나 실행됨
            생략 가능
"""
try:
    pass
except IndexError:
    print("인덱스가 맞지 않습니다")
except ZeroDivisionError:
    print("0으로 나누면 안됩니다")
else:
    print("예외가 발생하지 않았습니다")

print("프로그램이 정상적으로 종료됩니다")
print()

try:
    3 / 0
except IndexError:
    print("인덱스가 맞지 않습니다")
except ZeroDivisionError:
    print("0으로 나누면 안됩니다")
finally:
    print("예외에 상관없이 언제나 실행됩니다")

print("프로그램이 정상적으로 종료됩니다")
print("-------")

"""
*예외 발생시키기

raise 키워드를 사용하여 예외를 강제로 발생시킬수 있음
"""
#부모 클래스를 상속받는 자식 클래스에서 부모 클래스의 어떤 메소드는 반드시 구현하도록 만들도 싶음
'''
class watch:
    def day(self):
        raise NotImplementedError

class clock(watch):
    pass  #day() 메소드를 구현하지 않음

my_clock = clock()
my_clock.day()  #NotImplementedError가 강제로 발생
'''
class watch:
    def day(self):
        raise NotImplementedError

class clock(watch):
    def day(self):  #day() 메소드를 오버라이딩
        print("똑딱")

my_clock = clock()
my_clock.day()  #에러가 발생하지 않음

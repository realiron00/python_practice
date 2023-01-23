"""
*인수 전달 시 매개변수 지정

인수: 함수 선언 시 명시한 매개변수의 순서에 따라 언제나 순서대로 저장

전달받은 인수가 저장되는 매개변수를 직접 지정하고 싶다면, 대입연산자(=)를 사용
"""
def sub(a, b):
    print(a-b)

sub(1, 2)
sub(a=1, b=2)
sub(b=1, a=2)  #인수가 전달되는 순서를 매개변수를 지정하여 직접 변경
print("-------")

"""
*매개변수의 기본값 설정(default parameters)

미리 매개변수의 기본값을 설정 -> 전달받지 못한 인수에 대해서는 설정해 놓은 기본값으로 자동 초기화 가능
"""
def total(a, b=5, c=10):
    print(a + b + c)

total(1)  #1은 a에 저장, b와 c는 기본값인 5와 10을 사용
total(1, 2)  #1과 2는 a와 b에 저장, c는 기본값인 10을 사용
total(1, 2, 3)  #전달받은 인수의 값으로만 매개변수를 초기화
#total(b=2, c=3)->기본값을 설정하지 않은 매개변수에 인수를 전달하지 않음
#total(1, 2, 3, 4)->매개변수의 수보다 더 많은 인수를 전달
print("-------")
'''
def total(a=5, b, c=10):
   print(a + b + c)

total(1)
전달받은 인수 1은 매개변수 b가 아닌 매개변수 a에 저장
-> 매개변수 b에 저장할 인수가 없음 -> SyntaxError 발생

매개변수의 기본값 설정은 매개변수의 목록에서 항상 오른쪽부터 차례대로 명시되어야함
'''

"""
*가변 매개변수(variable parameters): 사용자가 직접 매개변수의 개수를 정할 수 있도록 하는 매개변수

매개변수명 앞에 별(*) 기호를 추가하여 선언

가변 매개변수에는 전달된 모든 인수가 튜플의 형태로 저장

문법:
def 함수명(*매개변수명):
   실행할 코드1
   실행할 코드2
"""
def add(*paras):
    print(paras)
    total = 0
    for para in paras:
        total += para
    return total

print(add(10))
print(add(10, 100))
print(add(10, 100, 1000))
print()
'''
가변 매개변수로 딕셔너리를 사용하려면, 두 개의 별(**)기호를 사용하여 선언
'''
def print_map(**dicts):
    for item in dicts.items():
        print(item)

print_map(이순신=100)
print_map(sun_sin=100, sejong=10000)
print_map(이순신=100, 세종=10000, 신사임당=50000)
print("-------")

"""
*여러 개의 결괏값 반환하기

두 개 이상의 결괏값을 반환하고 싶다면 튜플을 사용
"""
def a_n_s(a, b):
    add = a + b
    sub = a - b
    return add, sub  #하나의 튜플로 만들어 반환

i, j = a_n_s(10, 1)  #튜플의 언패킹을 통해 각각의 변수에 대입하여 사용 가능
print(i)
print(j)
print("-------")

"""
*람다(lambda): 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현한 것

이름을 가지지 않음, 함수 자체를 인수로 전달받는 함수(map(), filter() 함수)에서 자주 사용

문법:
lambda 매개변수1, 매개변수2, ...: 매개변수를 이용한 표현식
"""
def add(a, b):
    return a + b

print(add(1, 2))
print((lambda a, b: a+b)(1, 2))  #람다를 사용해 한 줄로 표현, 한 번밖에 사용 불가

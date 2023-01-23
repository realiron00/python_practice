"""
*변수의 유효 범위(variable scope): 변수가 선언된 위치에 따라 해당 변수가 영향을 미치는 범위

변수의 종류
1. 지역 변수(local variable)
2. 전역 변수(global variable)
"""

"""
*지역 변수(local variable): 함수 내에서 선언된 변수

함수 내에서만 사용 가능
특정 함수에서만 사용되는 값들은 지역 변수로 선언
"""
def func1():
    local_var = "지역 변수"  #지역 변수 선언
    print(local_var)

func1()
#print(local_var)->local_var은 함수의 호출이 끝남과 동시에 소멸, NameError 오류 발생
print("-------")

"""
*전역 변수(global variable): 함수 외부에서 선언된 변수

함수 외부에서 접근 가능, 모든 함수에서 global 키워드로 재선언하면 접근 가능
여러 함수에서 함께 사용하는 값들은 전역 변수로 선언
"""
def func2():
    global global_var  #global 키워드를 사용하여 전역 변수를 재선언
    local_var = "지역 변수"
    print(local_var)
    print(global_var)

global_var = "전역 변수"
func2()
print(global_var)
print()
'''
전역 변수와 지역 변수의 이름이 같은 경우에는 global 키워드를 사용하지 않을 경우, 별개의 변수로 취급
'''
def func3():
    var = "지역 변수"
    print(var)

var = "전역 변수"
print(var)
func3()
print(var)  #전역 변수 var의 값이 변하지 않음
print()

def func4():
    global var  #global 키워드를 사용->전역 변수의 값을 변경
    var = "지역 변수"
    print(var)

var = "전역변수"
print(var)
func4()
print(var)  #출력 결과가 "지역 변수"로 변경됨
'''
전역 변수의 값을 함수 내부에서 변경하는 것은 좋은 방법이 아님
->전역 변수를 사용하는 다른 함수의 동작을 의도치 않게 바꾸는 결과를 초래할 수 있음
'''

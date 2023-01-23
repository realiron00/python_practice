"""
*불리언 타입(boolean types): bool

불리언 타입: 참(True)과 거짓(False) 중 한가지만을 가질 수 있는 데이터 타입
1은 '참', 0은 '거짓'을 의미
"""
print(bool(1))         #True
print(bool(0))         #False

print(bool(None))      #False
print(bool([]))        #False
print(bool(()))        #False
print(bool({}))        #False
print(bool([1,2,3]))   #True

print(bool(""))        #False
print(bool("psycho"))  #True
print("-------")
#bool()함수: 인수로 전달된 데이터의 참과 거짓을 판단하여 반환
'''
문자열이나 리스트, 튜플, 딕셔너리 등이 비어있음-> 거짓으로 인식
문자열이나 리스트, 튜플, 딕셔너리 등이 비어있지 않음-> 참으로 인식
'''

"""
*비교 연산자(relational operator)

비교 연산자: 피연산자 사이의 상대적인 크기를 판단하는 연산자
<:  왼쪽의 피연산자가 오른쪽의 피연산자보다 작으면 True를 반환
<=: 왼쪽의 피연산자가 오른쪽의 피연산자보다 작거나 같으면 True를 반환
>:  왼쪽의 피연산자가 오른쪽의 피연산자보다 크면 True를 반환
>=: 왼쪽의 피연산자가 오른쪽의 피연산자보다 크거나 같으면 True를 반환
==: 왼쪽의 피연산자와 오른쪽의 피연산자가 같으면 True를 반환
!=: 왼쪽의 피연산자와 오른쪽의 피연산자가 같지 않으면 True를 반환
"""
i = 100
j = 24

print(i < j)   #False
print(i >= j)  #True
print(i == j)  #False
print(i != j)  #True
print("-------")

"""
*논리 연산자(logical operator)

논리 연산자: 주어진 논리식을 판단하여, 참과 거짓을 결정하는 연산자
or:  논리식 중에서 하나라도 True이면 True를 반환
and: 논리식이 모두 True이면 True를 반환
not: 논리식의 결과가 True이면 False를, False이면 True를 반환
"""
print((100 > 10) or (30 <= 3))  #True or False -> True
print((77 == 77) and (8 != 8))  #True and False -> False
print(not (5 <= 5))             #not True -> False

"""
*세트(set) = 집합

세트타입에서는 각 요소들의 순서를 매길 수 없음, 중복된 값을 허용하지 않음

중괄호({})로 감싸서 선언, 세트 안의 요소(element)들은 쉼표(,)로 구분
set() 함수: 문자열과 같이 순환할 수 있는 객체(iterable object)를 세트로 변환 가능

순환할 수 있는 객체: 저장된 요소를 하나씩 차례대로 반환할 수 있는 객체

문법:
세트명 = {요소1, 요소2, ...}
"""
set1 = {1, 2, 3}
set2 = set("Marvel")
set3 = set("Kookmin")

print(set1)
print(set2)
print(set3)  #증복된 값이 자동으로 제거
print("-------")
#출력 결과는 실행할 때마다 다르게 변함

"""
*빈 세트(empty set): 아무런 요소도 저장하고 있지 않은 집합

중괄호만으로 빈 세트를 나타내면 빈 딕셔너리로 잘못 인식

빈 세트는 중괄호가 아닌 set() 함수를 통해서만 선언 가능
"""
set1 = {}
set2 = set()

print(type(set1))  #빈 딕셔너리로 선언
print(type(set2))  #빈 세트로 선언
print("-------")

"""
*세트에 요소 추가하거나 제거하기

add() 함수: 전달된 인수를 해당 세트의 요소로 추가
remove() 함수: 해당 세트에서 전달된 인수를 찾아 제거

update() 함수: 여러 개의 요소를 한 번에 추가, 인수로는 순환할 수 있는 객체 타입만 전달 가능
"""
set1 = {1, 2, 3}

set1.add(4)
print(set1)

set1.update((5, 6))
print(set1)

set1.remove(2)
print(set1)
print("-------")

"""
*집합 연산

합집합, 교집합, 차집합, 여집합 등을 세트 타입을 활용하여 구현 가능
"""
set1 = {1, 2, 3, 4, 5}
set2 = set((1, 3, 5, 7, 9))

print(set1)
print(set2)

print(set1 | set2)  #합집합                    #1,2,3,4,5,7,9
print(set1 & set2)  #교집합                    #1,3,5
print(set1 - set2)  #차집합                    #2,4
print(set1 ^ set2)  #여집합 = 합집합 - 교집합  #2,4,7,9

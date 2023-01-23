"""
*딕셔너리(dictionary): 별도로 정의한 키(key)를 통해 각 요소에 접근할 수 있는 데이터 타입

딕셔너리에서는 키를 가지고 그 키에 해당하는 값(value)을 찾을 수 있음

딕셔너리 = 맵(map)
"""

"""
*딕셔너리 선언하기

중괄호({})로 감싸서 선언, 각 요소(element)들은 쉼표(,)를 사용하여 구분
딕셔너리의 요소는 키와 값의 한 쌍으로 구성, 이 둘은 콜론으로 연결

문법:
딕셔너리명 = {요소1, 요소2, ...}
요소 = 키: 값
"""
dict1 = {'십원': 10, '만원': 'sejong', '파이': 3.14}
dict2 = dict({'십원': 10, '만원': 'sejong', '파이': 3.14})
dict3 = dict({('십원', 10), ('만원', 'sejong'), ('파이', 3.14)})
dict4 = dict(십원=10, 만원='sejong', 파이=3.14)  #대입 연산자를 사용하기 위해서는 키가 문자열이어야 함

print(dict1)
print(dict2)
print(dict3)
print(dict4)
print()
'''
딕셔너리의 키: 정수, 문자열, 실수 등 사용 가능
               변경할 수 있는 타입(mutable types)(리스트, 딕셔너리)의 값은 사용 불가
'''
dict1 = {'하나': 1, 2: 'two', 3.14: 'pi'}
dict2 = {('ten', 10): ['열', 10.0]}  #튜플: 값을 변경할 수 없는 타입->딕셔너리의 키로 사용 가능

print(dict1)
print(dict2)
print("-------")

"""
*딕셔너리 사용하기

대괄호([])를 사용하여 키를 전달 -> 해당 키로 저장된 값을 얻을 수 있음
: 존재하지 않는 키에 대해 KeyError 발생, 프로그램 강제 종료

get() 함수를 사용해도 같은 결과를 얻을 수 있음
: 존재하지 않는 키에 대해 정상적으로 종료, None을 반환
"""
dict1 = dict({'삼성': 80, 'LG': 90, 'APPLE': 70})

print(dict1['삼성'])
print(dict1.get('삼성'))

# print(dict1['샤오미'])->강제 종료
print(dict1.get('샤오미'))
print("-------")

"""
*딕셔너리에 요소 추가하거나 제거하기

딕셔너리에 요소 추가: 대괄호 안에 키를 넣고 대입연산자(=)를 사용하여 값을 저장
dict['키값'] = 값

del 키워드: 딕셔너리의 특정 요소 제거
clear() 함수: 딕셔너리에 저장된 모든 요소들을 한 번에 삭제
"""
dict1 = dict({'삼성': 80, 'LG': 90, 'APPLE': 70})
dict1['샤오미'] = 50
print(dict1)

del dict1['LG']
print(dict1)

dict1['삼성'] = 100  #이미 저장되어 있는 키와 동일한 키를 사용하여 요소 추가->추가한 값만 저장
print(dict1)

dict1.clear()
print(dict1)
print("-------")

"""
*딕셔너리의 정보 얻기

key() 함수: 딕셔너리에 저장된 모든 요소의 키들을 한 번에 얻을 수 있음
->반환값: dict_keys
values() 함수: 딕셔너리에 저장된 모든 요소들의 값들을 따로 얻을 수 있음
->반환값: dict_values
items() 함수: 딕셔너리에 저장된 모든 요소들을 각각 키와 값의 한 쌍으로 이루어진 튜플의 형태로 반환
->반환값: dict_items

반환값 객체들은 list() 함수를 사용하여 리스트 타입으로 변환하여 사용 가능
"""
dict1 = dict({'토르': 80, 'ironman': 90, 'captain': 70})

print(dict1.keys())
print(dict1.values())
print(dict1.items())

print('ironman' in dict1)  #ironman이라는 키가 포함->True
print('앤트맨' in dict1)   #'앤트맨'이라는 키가 불포함->False

"""
*튜플(tuple): 여러 개의 데이터를 하나로 묶는데 사용

1. 튜플은 그 값을 변경할 수 없음(immutable type)
2. 튜플은 다른 데이터 타입에 비해 그 실행 속도가 빠름

그 값을 일정하게 유지해야 함 -> 튜플로 작성
도중에 그 값이 변경되거나 변경될지도 모르는 데이터 -> 리스트로 작성
"""

"""
*튜플 선언하기

대괄호 대신 소괄호(())로 감싸거나 아예 감싸지 않고 선언

문법:
튜플명 = (요소1, 요소2, ...) or 튜플명 = 요소1, 요소2, ...
"""
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3  #소괄호를 사용하지 않아도 자동으로 튜플로 인식

tuple3 = (1, )
tuple4 = (1)  #쉼표를 생략하면 하나의 데이터로만 인식

print(tuple1)
print(tuple2)

print(tuple3)
print(tuple4)
print("-------")

"""
*튜플 사용하기

값 변경 불가 ->요소를 추가, 삭제, 삽입, 추출하는 동작 등은 수행 불가
"""
tuple1 = (1, 2, 3)
tuple2 = tuple(["일", "이", "삼"])  #tuple() 함수를 사용해 선언
#tuple() 함수의 인수로는 순환할 수 있는 객체(iterable object)만을 사용 가능

#튜플 요소 선택하기
print(tuple1[0])
print(tuple2[-1])

#튜플 자르기
print(tuple1[1:])
print(tuple2[:2])

#튜플끼리의 연산
print(tuple1 + tuple2)
print(tuple1 * 2)
print("-------")

"""
*패킹(packing)과 언패킹(unpacking)

패킹: 여러 타입의 데이터를 하나의 튜플이나 리스트로 묶어 선언하는 것
언패킹: 하나의 튜플이나 리스트의 요소들을 여러개의 변수로 나누어 대입하는 것
"""
#패킹(packing)
tuple1 = 10, "열", True  #둘 이상의 데이터가 쉼표로 연결되어 있으면, 하나의 튜플로 패킹

#언패킹(unpacking)
a, b, c = tuple1  #둘 이상의 변수에 튜플의 각 요소들을 한 번에 언패킹 가능
'''
a, b, c, d = tuple1
a, b = tuple1
변수의 개수가 튜플이나 리스트의 길이와 다를 경우 ValueError 발생
언패킹을 할 때 변수의 개수와 길이가 일치하는지 확인해야 함
'''
print(a)
print(b)
print(c)
print("-------")

"""
*특정 요소의 포함 여부

in 키워드 사용
해당 데이터에 특정 요소가 포함 -> 참 반환
                          포함되어 있지 않음 -> 거짓 반환
"""
tuple1 = 10, "열", True

print(10 in tuple1)
print("아홉" in tuple1)
print("아홉" not in tuple1)  #not in 키워드는 in 키워드와 반대로 반환

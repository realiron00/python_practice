"""
*리스트(list)

1. 리스트에 저장되는 요소가 모두 같은 타입일 필요는 없음
2. 리스트에는 요소들이 순서대로 저장, 각 요소는 0부터 시작하는 인덱스(index)를 사용하여 접근 가능
3. 리스트는 그 값을 변경 가능(mutable type)

다른 프로그래밍 언어에서는 배열이라고 부름
"""

"""
*리스트 선언하기

대괄호([])로 감싸서 선언
리스트 안의 요소(element)들은 쉼표(,)로 구분

문법:
리스트명 = [요소1, 요소2, ...]
"""
primes = [2, 7, 13, 17]

for p in primes:
    print(p)

print(len(primes))
#len() 함수를 사용하면 리스트에 저장된 모든 요소의 개수를 손쉽게 알 수 있음
print("-------")

"""
*리스트 요소 선택하기

리스트의 특정 요소에만 접근하고 싶을 때에는 0부터 시작하는 인덱스를 사용해야만 함
"""
primes = [2, 3, 5, 7]

print(primes[0])
print(primes[-1])  #prime[-1] = primes[3]
print(primes[1] + primes[3])
#print(primes[5]) -> IndexError가 발생하며 강제 종료
print("-------")

"""
*리스트 자르기

리스트 일부분만 선택하거나 일부 요소들만 수정해야 할 경우 슬라이싱
"""
list1 = [1, 2, 3, 4, 5]

print(list1[3])
print(list1[1:3])  #콜론의 앞쪽에 위치한 인덱스부터 뒤쪽의 위치한 인덱스 바로 앞까지의 요소를 반환
print(list1[:3])
print(list1[3:])
#콜론(:)기호를 사용하면 리스트의 일부분만 자를 수 있음
print(list1)  #원본 리스트에는 영향을 미치지 않음
print("-------")

"""
*리스트 복사하기
"""
list1 = [1, 2, 3, 4, 5]

copy = list1[:]  #리스트 list2의 모든 요소를 선택하여 자르는 구문
copy.append(6)
#잘린 리스트는 원본 리스트와는 별도의 리스트로 반환됨

print(copy)  #리스트가 제대로 복사됨
print(list1)
print("-------")

"""
*리스트끼리의 연산

더하기(+) 연산: 두 리스트를 서로 연결
리스트와 정수의 곱하기(*) 연산: 해당 리스트의 모든 요소들을 정수배만큼 반복해서 연결
"""
list1 = [1, 2, 3]
list2 = list((4, 5, 6))  #list() 함수를 사용해 리스트 선언
#list() 함수의 인수로는 순환할 수 있는 객체(iterable object)만을 사용 가능

print(list1 + list2)
print(list1 * 3)

list1.extend(list2)  #extend() 함수: 더하기 연산과 마찬가지로 하나의 리스트에 다른 리스트를 연결
print(list1)  #extend() 함수는 원본 리스트 자체를 변경함
print("-------")

"""
*리스트에 요소 추가하거나 제거하기

append() 함수: 전달된 인수를 해당 리스트의 마지막 요소로 추가
remove() 함수: 전달된 인수를 해당 리스트에서 찾아 제거
"""
list1 = [1, 2, 3, 4, 5]

list1.append(2)
print(list1)

list1.remove(3)
print(list1)

list1.remove(2)  #전달한 요소가 두 개 이상 존재할 경우, 인덱스가 가장 낮은 요소 하나만을 삭제
print(list1)
print("-------")

"""
*리스트에 요소 삽입하거나 꺼내기

insert() 함수: 해당 리스트의 지정된 인덱스에 전달된 인수를 요소로 삽입
pop() 함수: 전달받은 인덱스에 위치한 요소를 리스트에서 추출하여 반환
"""
list1 = [1, 2, 3, 4, 5]

list1.insert(3, 9)  #첫 번째 인수로 요소를 삽입할 인덱스를 전달, 두 번째 인수로 삽입할 요소를 전달받음
print(list1)

list1.pop(4)
print(list1)
print("-------")

"""
*리스트 뒤집거나 정렬하기

reverse() 함수: 리스트의 모든 요소를 역순으로 뒤집어서 반환
sort() 함수: 리스트의 모든 요소를 순서대로 정렬
"""
list1 = [5, 2, 4, 1, 3]
list2 = [5, 2, 4, 1, 3]

list1.reverse()
print(list1)

list1.sort()
print(list1)

print(sorted(list2))  #sorted() 함수: 원본 리스트는 변경하지 않고 정렬된 새로운 리스트를 반환
print(list2)
print("-------")

"""
*중첩 리스트

리스트의 요소로 또 다른 리스트 추가 가능
중첩된 안쪽 리스트의 특정 요소의 인덱스: 두개의 대괄호([][])를 사용하여 표시
"""
matrix = [[1, 2, 3], ["일", "이", "삼"]]

print(matrix[0])
print(matrix[0][1])
print(matrix[1][2])
#c언어의 이차원 배열과 비슷

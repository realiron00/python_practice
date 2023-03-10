"""
*변수(variable)

변수: 프로그램에서 사용되는 데이터를 저장해 놓는 공간
      데이터를 저장할 수 있도록 이름을 할당받은 메모리 공간
      언제든지 다시 접근하거나 값 변경 가능
"""

"""
*변수의 사용
"""
damoim = "내년엔 잘될거야 아마두"  #변수 선언, 대입 연산자(=)를 사용->해당 변수에 문자열을 저장

print(damoim)
print(damoim)
print(damoim)  #변수 사용시 중복해서 작성해야 하는 코드가 줄어듦
print("-------")

"""
*변수의 재활용
"""
damoim = "택배가 도착할걸 아마두"  #대입 연산자를 사용하여 다른 값으로 변경

print(damoim)
print(damoim)
print(damoim)

"""
*변수명 생성 규칙

1. 영문자(대소문자), 숫자, 언더스코어(_)로만 작성 가능
2. 숫자로 시작 불가->반스기 영문자나 언더스코어로 시작
3. 대소문자 구분 가능
4. 파이썬에서 미리 정의된 예약어(reserved words)는 사용 불가
"""

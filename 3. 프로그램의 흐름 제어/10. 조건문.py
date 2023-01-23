"""
*조건문: 주어진 조건식의 결과에 따라 다른 명령을 수행하는 프로그램의 흐름을 제어하는 명령문
"""

"""
*if-else 문

문법:
if 조건식: 조건식의 결과가 참(True)일 때만 실행되는 명령문
else: 조건식의 결과가 거짓(false)일 때만 실행되는 명령문

if 키워드 뒤에 위치한 조건식의 결과에 따라 실행되는 명령문이 달라짐
if 키워드와 else 키워드의 맨 끝에도 반드시 콜론(:)을 삽입
"""
con = "marvel"

if con == "marvel":
    print("꿀잼")
else:
    print("노잼")
print("-------")

"""
*if-elif-else 문

elif 키워드: else if의 줄임말

문법:
elif 조건식2:
     조건식2의 결과가 참일 때만 실행되는 명령문
"""
season = "summer"

if season == "spring":
    print("봄이면 씨앗뿌려")
elif season == "summer":
    print("여름이면 꽃이피네")
elif season == "fall":
    print("가을이면 풍년되어")
elif season == "winter":
    print("겨울이면 행복하네")
#elif 문을 사용하면 코드가 간결해지며 가독성 또한 높아짐
print("-------")
#switch-case 문을 파이썬에서는 제공하지 않음

"""
*pass 키워드로 아무 일도 하지 않기

pass라는 키워드는 다른 어떤 동작도 수행하지 않음
"""
temp = 36

if temp<38:
    pass  #pass문을 삭제하면 IndentationError 에러 발생
else:
    print("몸에 이상이 있음")

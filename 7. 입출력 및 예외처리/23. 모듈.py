"""
*모듈(module): 정의했던 변수, 함수, 클래스 등을 다른 파이썬에서 불러오도록 하나의 파일로 모아놓는 방법
               파이썬 사용할 수 있는 여러 정의들과 실행 가능한 구문들을 담고 있는 파이썬 파일(.py)

다른사람이 만든 모듈을 사용하거나 자신이 직접 새로운 모듈을 작성하여 사용 가능
"""

"""
*모듈 불러오기

import 문을 사용하여 모듈 불러오기 가능
통상적으로 코드의 맨 앞에 위치하는 것이 좋음

문법:
1. import 모듈명 -> 모듈에 포함된 변수나 함수를 사용할 때마다 매변 모듈명과 함께 닷(.) 연산자 사용
2. from 모듈명 import * -> 변수명이나 함수명만으로도 간편하게 사용 가능
=>1, 2 모두 해당 모듈 전체를 불러옴
3. from 모듈명 import 함수명 or 클래스명
"""
#수학 관련 모듈인 math 모둘을 임포트해서 사용
import math

print(math.pi)
print(math.pow(2, 4))
#모듈명인 math와 닷(.)연산자까지 함께 사용

from math import *

print(pi)
print(pow(2, 4))
#모듈명을 사용하지 않고 변수명이나 함수명 만으로 간단하게 사용 가능
print()

e = "내가 정의한 변수 e"
print(e)

from math import *
print(e)  #내가 정의한 변수 e에는 접근 불가(math모듈에 오일러의 수가 같은 이름으로 포함됨)
print(pi)
print()

e = "내가 정의한 변수 e"
print(e)

from math import pi  #필요한 변수나 함수만(pi)을 불러옴
print(e)
print(pi)
#내가 정의한 변수명과 모듈러의 변수명이 겹치는 경우를 막을 수 있음

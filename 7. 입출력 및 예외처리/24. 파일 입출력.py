"""
*파일 입출력

파일에 저장된 내용을 읽고 쓰는 동작: 파일 객체(file object)를 사용
"""

"""
*파일 열고 닫기

open() 함수를 사용하여 파일을 열 수 있음

문법:
파일객체 = open(파일명, 파일모드문자열)
-첫 번째 인수: 열고자 하는 파일의 이름과 경로를 문자열 형태로 전달
-두 번째 인수: 파일의 사용 용도를 결정하는 파일 모드 문자열을 전달

open() 함수는 파일 객체를 반환, 파일 객체를 가지고 다양한 파일 입출력 작업 가능

파일 입출력 작업이 끝나면 close() 함수를 사용하여 파일 객체를 닫아줘야 함
"""

"""
*파일 모드 문자열

첫번째, 파일의 사용 용도를 결정하는 문자열이 나옴
생략할 경우 파일은 읽기 전용 모드(read mode)로 열림
1. r(read mode): 읽기 전용 모드(기본값)
2. w(write mode): 쓰기 전용 모드
3. a(append mode): 파일의 마지막에 새로운 데이터를 추가하는 모드

두번째, 파일의 데이터를 어떤 방식으로 입출력할지를 결정하는 문자열이 이어짐
이를 생략하면 파일은 텍스트 모드(text mode)로 열림
1. t(text mode): 해당 파일의 데이터를 텍스트 파일로 인식하고 입출력 함
2. b(binary mode): 해당 파일의 데이터를 바이너리 파일로 인식하고 입출력함

세번째, 파일 모드 문자열 추가 가능
1. x(exclusive mode): 열고자 하는 파일이 이미 존재하면 파일 개방에 실패함
2. +(update mode): 파일을 읽을 수도 있고 쓸 수도 있도록 개방함
"""

"""
*파일 내용 읽기

1. read() 함수: 해당 파일의 모든 내용을 읽어 들여 하나의 문자열로 반환
2. readline() 함수: 해당 파일의 내용을 한 라인씩 읽어 들여 문자열로 반환
                    파일의 끝(EOF)에 도달하여 더 이상 가져올 라인이 없을 경우 None 반환
3. readlines() 함수: 해당 파일의 모든 라인을 읽어 각 라인을 하나의 요소로 저장하는 하나의 리스트 반환
"""
'''
anysong.txt:
아무 노래나 일단 틀어
아무거나 신나는 걸로
아무렇게나 춤춰
아무렇지 않아 보이게
'''
fp = open('anysong.txt', 'r')

text = fp.read()
print(text)

fp.close()
print()

fp = open('anysong.txt', 'r')

while True:
    file_line = fp.readline()
    if not file_line:
        break
    print(file_line, end='')
#파일의 모든 내용을 읽기 위해서는 반복문을 사용해야 함

fp.close
print()
print()

fp = open('anysong.txt', 'r')

file_lines = fp.readlines()
print(file_lines)

fp.close()
#readlines() 함수를 사용하여 파일 내용을 읽어들일 때에는 개행 문자('\n')까지 모두 함께 저장됨
print("-------")

"""
*파일에 내용 추가하기

같은 이름의 파일이 이미 존재하면, 해당 파일에 저장되어 있는 모든 내용을 제거 후 파일을 열음
기존에 존재하는 파일에 새로운 내용을 추가하려면 파일 모드 문자열을 'a'로 전달해서 파일을 열어야힘

write() 함수 사용
"""
fp = open('anysong.txt', 'a')

fp.write("\n")
fp.write("\n아무 생각 하기 싫어")

fp.close()
print("-------")

"""
*자동으로 파일 닫기

with 문: 개방한 파일을 자동으로 닫아줌
         해당 with 블록을 벗어남과 동시에 개방되었던 파일 객체를 자동으로 닫아줌
         일일이 닫는 수고를 덜어줌, 코드의 가독성 향상

문법:
with open(파일명, 파일모드문자열) as 파일객체:
    수행할 명령문
"""
with open('anysong.txt', 'r') as fp:
    file_data = fp.read()
    print(file_data)

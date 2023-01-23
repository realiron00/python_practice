"""
*break 키워드로 반복문 탈출하기

break 키워드를 사용하여 반복 조건에 상관없이 가장 가까운 반복문을 즉시 탈출 가능
"""
for col in range(2, 10):
    if col > 5:
        break
    for row in range(1, 10):
        print(col, "X", row, "=", col * row)
#5단까지만 출력
print("-------")

"""
*continue 키워드로 처음으로 되돌아가기

continue 키워드: 해당 루프만을 즉시 종료하고 다음 루프를 실행
"""
for n in range(1, 11):
    if n % 2 == 0:  #n이 짝수인 경우
        continue  #해당 반복을 중지, n의 크기를 1 증가시킴
    print(n, "은 홀수입니다.")

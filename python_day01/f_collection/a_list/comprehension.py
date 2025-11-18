# Comprehension(컴프리헨션: 이해력, (어떤 뜻을) 내포[포함])
# 반복되거나 특정 조건을 만족하는 리스트를 보다 쉽게 만들어 내기 위한 방법

# List Comprehension 구문
# [표현식 for 변수 in iterator (if 조건)]

datas = [1, 2, 3, 4]
print(datas * 3)

result = [i * 3 for i in datas]
print(result)

result = [i for i in result if i % 2 == 0]
print(result)

print("*" * 50)

# 아래 List의 요소 중 '양수'만 추출하여 새로운 리스트 만들기
datas = [10, 20, 30, -20, -3, 50, -70]
result = [data for data in datas if data > 0]
print(result)

# 제곱의 결과가 10보다 큰 값만 담은 List
datas = [1, -2, 3, -4, 5]
result = [data for data in datas if data**2 > 10]
print(result)

# 0 ~ 9까지 중 3의 배수만 List에 담고 출력
result = [i for i in range(10) if i % 3 == 0]
print(result)
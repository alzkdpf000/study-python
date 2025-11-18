a = 11
b = 33
print(type(a))
print(type(b))

# a와 b에 있는 값을 서로 바꾼다.
temp = a
a = b
b = temp
print(a, b)

(a, b) = (b, a)
print(a, b)

format = "{}, {}, {}".format(1, 2, 3)
print(format)

# 변수 3개 선언해서 format으로 출력하기
a = 10
b = 20
c = 30
format = "{}, {}, {}".format(a, b, c)
print(format)

format = "{2}, {0}, {1}".format(1, 2, 3)
print(format)

format = ("{number3}, {number2}, {number1}"
          .format(number1=1, number2=2, number3=3))
print(format)

# 실습
# 이름과 나이를 변수에 담는다
# format()을 사용해서 출력
name = "한동석"
age = 20
format = "{name}, {age}".format(name=name, age=age)
print(format)

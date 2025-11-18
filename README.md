# Python 기초 정리

## 🐍 Python이란?

컴퓨터와 소통하기 위한 프로그래밍 언어로, **간결한 문법과 높은 생산성** 때문에 인기 있는 언어이다.

- GUI 개발  
- 웹 개발  
- 데이터 분석  
- AI/머신러닝  

등 다양한 분야에서 사용된다.

---

## 🖥️ 일반 프로그램 동작 구조

프로그램
↓
OS(운영체제)
↓
하드웨어
👉 일반 프로그램은 이식성이 좋지 않다.

---

## 🐍 Python 프로그램 구조

프로그램
↓
PVM(Python Virtual Machine)
↓
OS
↓
하드웨어
👉 Python 프로그램은 이식성이 좋다.


---


# 🔢 변수(Variable)

변수는 **값을 저장하는 메모리 공간**이다.

```python
x = 10
```

RAM에 x라는 이름의 공간이 생성되고 값 10이 저장된다

| 자료형   | 예시             |
| ----- | -------------- |
| int   | 0, 10, -5      |
| float | 0.1, 2.5       |
| str   | "Hi", 'Python' |
| list  | [1, 2, 3]      |
| tuple | (1, 2), (1,)   |
| dict  | {"name": "A"}  |
| set   | {1, 2, 3}      |
| bool  | True, False    |


# 📝 변수명 규칙
-  문자로 시작
-  특수문자 사용 불가 (_만 가능)
-  공백 사용 불가
-  소문자 권장
-  의미 있는 단어 사용
-  ❌ a, b, c
-  ✔️ age, count, username

# ✍️ 표기법

| 표기법        | 형태          | 사용처          |
| ---------- | ----------- | ------------ |
| PascalCase | PythonClass | 클래스 이름       |
| camelCase  | userName    | Java 변수/함수   |
| snake_case | user_name   | Python 변수/함수 |
| kebab-case | user-name   | HTML/CSS     |


# 🧩 서식문자
따옴표 안에서 변수 또는 값을 표현할 때 사용

| 서식문자 | 설명  |
| ---- | --- |
| %d   | 정수  |
| %f   | 실수  |
| %s   | 문자열 |


# 🔄 형변환
int(), float(), str(), bool(), bin(), oct(), hex()

# ➗ 연산자
## 1. 산술 연산자

| 연산자 | 설명  |
| --- | --- |
| +   | 더하기 |
| -   | 빼기  |
| *   | 곱하기 |
| /   | 나누기 |
| **  | 제곱  |
| //  | 몫   |
| %   | 나머지 |

## 2. 대입(복합 대입) 연산자

| 연산자 | 예시      |
| --- | ------- |
| =   | x = 10  |
| +=  | x += 10 |
| -=  | x -= 10 |
| *=  | x *= 10 |
| /=  | x /= 10 |
| **= | x **= 2 |
| //= | x //= 2 |


## 3. 비교 연산자

| 연산자 | 설명    |
| --- | ----- |
| ==  | 같다    |
| !=  | 같지 않다 |
| >   | 크다    |
| <   | 작다    |
| >=  | 이상    |
| <=  | 이하    |

## 4. 논리 연산자

| 연산자 | 설명        |
| --- | --------- |
| and | 둘 다 True  |
| or  | 하나라도 True |
| not | 반전        |

## 5. 멤버 연산자
| 연산자    | 설명     |
| ------ | ------ |
| in     | 포함 여부  |
| not in | 미포함 여부 |

## 6. 식별 연산자

| 연산자    | 설명      |
| ------ | ------- |
| is     | 같은 객체인지 |
| is not | 다른 객체인지 |

# 🔀 제어문
## ✔ if
```python
if 조건:
    실행문
elif 조건:
    실행문
else:
    실행문
```




# 🔁 반복문
## for
```python
for 변수 in range(start, end, step):
    실행문
```
## while
```python
while 조건:
    실행문
```

# 📦 리스트(list)
여러 값을 순서대로 저장하는 구조.
## 선언
```python
data = [1, 2, 3]
data = [0] * 5
data = list(range(1, 10))
```
## 주요 기능
### 값 추가/삽입
```python
data.append(4)
data.insert(1, 100)
```
### 값 삭제
```python
data.remove(1)
del data[0]
data.clear()
```
### 값 검색
```python
data.index(3)
```
### 값 수정
```python
data[0] = 10
```
# 🗂 딕셔너리(dict)
Key-Value 형태로 저장.
## 선언
```python
user = {"name": "John", "age": 20}
```
### 추가/수정
```python
user["gender"] = "M"
user.update({"age": 30})
```
### 삭제
```python
del user["age"]
```
### 검사
```python
"name" in user
```

---

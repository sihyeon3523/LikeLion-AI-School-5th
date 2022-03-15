## if 문
---
- 리스트와 딕셔너리 안에 있는 값인지 확인할 때 "in" 사용
```python
orders = ["짜장","짬뽕", "탕수육"]

if "짜장" in orders:
    print("먹고싶다")

orders_dict = {"짜장": "No", "짬뽕":"yes", "탕수육":"no?"}

if "짜장" in orders_list:
    print(orders_list["짜장"])
else:
    print("아니에요")
```
### 비교 연산자
- !=
- ==
- ">"
- "<"


## 반복문
---
- while, for 문 사용
- 무한루프를 끝내기 위해서 ctrl+c 사용
- break 문으로 반복문을 원하는 시점에 나갈 수 있음
  
```python
i = 0
while True:
    print(i)
    i = i+ 1
    
    if i >= 3:
        break

print("반복문 종료")
```
- continue 문으로 건너뛰기 가능
```python
i = 0

while i < 10:
    i = i + 1

    # 2의 배수일 경우 출력 안하고 다음 while문 실행
    if i%2 == 0:
        continue
    print(i) 
```
- range(시작값, 끝 값 +1, step) 사용
```python
# "Hi"가 3번 출력 
for x in range(3):
    print("Hi")
```
### 확장 문자 출력 
print(value, end= " ") 할 때 end 안에 print하려는 문자 끝을 어떻게 출력할 것인지 설정할 수 있다
- \n : newline 문
- \t : tab 문자
- " "
```python
for i in range(1, 10):
    print(i, end="\t") # 
```

### random 함수 사용
```python
```
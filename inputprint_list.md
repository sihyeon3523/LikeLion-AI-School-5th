## input 과 print
---
- input 받을 때 데이터 타입은 str이다
- 정수형으로 바꿔주기 위해서는 int( ) 사용
  
```python
food = input("나이?")
food = int(food)
```

## 리스트
---
- data = [ ] 형태로 정의
- 리스트 안의 각각의 데이터를 "요소"라고 부름
- 순서 부여하며 index 가 있음 (0번부터 index 시작)
- 문자열에서 띄어쓰기도 하나의 문자열

### 리스트 함수
```python
array = [1,2,3,4]

# 리스트에 원소를 하나 삽입 
array.append(5)

# 인덱스로 접근하여 데이터 삭제 
del array[-1]

# 특정 값을 갖는 원소 제거, 값을 가진 원소가 여러 개 일경우 하나만 제거
array.remove(3)

# 오름차순 정렬
array.sort()

# 내림차순 정렬
array.sort(reverse=True)

# (삽입할 위치 인덱스, 삽입할 값) 특정 위치에 원소 삽입
array.insert(1, 4)

# 특정 값을 가지는 데이터 갯수 세기 
array.count(4)

# 리스트 길이
print(len(array))
```

### 내장함수
- import 명령 없이 바로 사용할 수 있는 내장 함수

```python
# 합 
result = sum([1,2,3,4])

a = [1,2,3,4]
result = sum(a)

# 평균
result = sum(a) / len(a)

# 최소값
result = min([1,2,3,4])

# 최대값
result = max([1,2,3,4])
```
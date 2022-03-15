
## 함수
---
- 미리 정의된 작업으로 필요할 때 호출한다
- 언제나 똑같이 결과물을 뽑아야 할 때 사용!

```python
def make_shake():
    print("hey, I'm Done!")

make_shake()
```

## 딕셔너리  
---
- {"key" : "value"} 형태로 저장 
- key 값으로 데이터 접근 
  
딕셔너리 함수
```python
age = {"사람1":40, "사람2":43, "사람3": 8, "사람4": 12}

# 딕셔너리에서 값 삭제
del age['사람4']

# 값 수정
age['사람3'] = 25
```
```python
have_to_do = {}

while True: 
    what = input("오늘 할 일은?" : )
    if what == nothing:
        break
    else:
        # what을 key로 갖는 dict 만들기 
        have_to_do[what] = "" 

for i in have_to_do:
    print(i)
    how = input("어떻게 할껀데?")
    have_to_do[i] = how

print(have_to_do)
```

```python
have_to_do = []

while True:
    what = input("오늘 할 일은?" : )
    if what == nothing:
        break
    else:
        # value 없는 dict 초기화 방법 
        have_to_do.append({"할 일": what, "어떻게": ""})

for i in have_to_do:
    print(i["할 일"])
    how = input("어떻게 할껀데?")
    i['어떻게'] = how

print(have_to_do)
```

### 03. Stack  스택 

![image-20220910124808441](C:\Users\LGD\AppData\Roaming\Typora\typora-user-images\image-20220910124808441.png)

* **데이터를 제한적으로 접근할 수 있는 구조 (한쪽 끝에서만 자료를 넣거나 뺼 수 있는 구조 )**

* **가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조** **(큐 FIFO vs 스택 LIFO)**

* **FIFO : 마지막에 넣은 데이터를 가장 먼저 추출하는 데이터 관리정책**

* **FILO : 처음에 넣은 데이터를 가장 마지막에 추출하는 데이터 관리 정책 **

* **대표적 활용 : 컴퓨터 내부의 프로세스 구조의 함수 동작 방식**

* **push() : 데이터를 스택에 넣기**

* **pop() : 데이터를 스택에서 꺼내기**

  

> 스택 구조는 프로세스 실행 구조의 가장 기본 
>
> 함수 호출 시 프로세스 실행 구조를 스택과 비교해서 이해 필요 



![image-20220910131749615](C:\Users\LGD\AppData\Roaming\Typora\typora-user-images\image-20220910131749615.png)

```python
# 재귀함수 
def resursive(data):
    if data < 0:
        print("ended")
    else: 
        print(data)
        recursuve(data-1) # data-1 을 하면서 자기 자신 호출
        print("returned", data)
```

```python
recursive(4)
#4
#3
#2
#1
#0
#ended
#returned 0
#returned 1
#returned 2
#returned 3
#returned 4
```



---



#### ◼ 스택의 장단점 

|                       장점                        |            단점 _ 일반적인 스택 구현 시             |
| :-----------------------------------------------: | :-------------------------------------------------: |
| 구조 단순, 구현  easy! 데이터 저장/읽기 속도 빠름 | 데이터 최대 갯수 미리 저장해야함 / 저장 공간의 낭비 |



#### ◼ 파이썬 리스트 기능에서 제공하는 메서드로 스택 사용

> append(push), pop 메서드 제공

```python
data_stack = list()

data_stack.append(1)
data_stack.append(2)

# data_stack 
# [1, 2]
# 여기서 1은 append할때 맨 처음으로 들어옴 
# 여기서 2는 pop 할때 마지막으로 들어옴

# data_stack.pop()
```



#### ◼ **pop, push 함수 사용하지 않고 직접 구현**

```python
stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data
```

```python
for index in range(10):
    push(index)
```

```python
pop()
#9
```


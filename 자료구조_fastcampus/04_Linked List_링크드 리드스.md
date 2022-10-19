### 04. Linked List 링크드 리스트 

![image-20220910135717777](C:\Users\LGD\AppData\Roaming\Typora\typora-user-images\image-20220910135717777.png)

* **Linked List는 연결리스트라고도 불림**
* **Linked List VS Array**
  * 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조 
  * 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조 
  * C언어는 주요한 데이터 구조이지만 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원



* **NODE** : 데이터 저장단위 (데이터 값, 포인터)로 구성 (**구현 시 파이썬 객체지향 문법 이해 필요**)
* **Pointer** : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간 



#### ◼ Node 구현

> 2가지 정보를 저장해야 하기 떄문에 clsss가 적절하다

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

```python
# 위의 코드보다 조금 더 복잡한 구조이다. 
class Node:
    def __init__(self, data, next=None):
        # None 디폴트 값 
        # next=(None) : 다음 가는 주소값
        self.data = data
        self.next = next
```



#### ◼ 링크드 리스트의 장단점 

|                           장점                            |                 단점 _ 일반적인 스택 구현 시                 |
| :-------------------------------------------------------: | :----------------------------------------------------------: |
|        미리 데이터 공간을 미리 할당하지 않아도 됨         | 연결을 위한 별도 데이터 공간이 필요하므로, 저장 공간 효율이 높지 않음 |
| (반면, 배열은 미리 데이터 공간을 할당해야하는 점이 있다.) |    연결 정보를 찾는 시간이 필요하므로 접근 속도가 느리다.    |
|                             -                             | 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요 |



![image-20220910161747414](C:\Users\LGD\AppData\Roaming\Typora\typora-user-images\image-20220910161747414.png)



#### ◼ Node 와 Node 연결하기 (포인터 활용)

```python
node1 = Node(1)
node2 = Node(2)
node1.next = node2 # 가장 맨앞의 노드 주소값을 알아야하기 때문에 node1
head = node1
```



#### ◼ 링크드 리스트로 데이터 추가하기

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:#마지막 노드를 찾기 위해 작성 
        node = node.next#마지막 노드를 찾기 위해 작성 
    node.next = Node(data) 
```

```python
node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index) 
```



#### ◼ 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현

> 복잡한 리스트 구현과 다양한 링크드 리스트 구조도 꼭 코드 직접 작성해보기 

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        
    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next
```

```python
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
```

```python
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()
```



---



####  ✍필기 내용

* **특정 노드를 삭제 하는 경우 3가지**
  * HEAD 삭제 
  * 마지막 노드 삭제 
  * 중간 노드 삭제 
* **다양한 Linked List 구조**
  * Double linked list  (=  이중 연결 리스트)
  * 장점 : 양방향으로 연결되어 있어서 노드 탐색이 양쪽으로 모두 가능하다. 

![image-20220910162121632](C:\Users\LGD\AppData\Roaming\Typora\typora-user-images\image-20220910162121632.png)



* **이중 리스트 이기 떄문에 head(시작), tail(끝)이있다. _ head와 tail 에는 똑같이 해당 데이터를 가진다.** 



* **insert 라는 메소드 **
  * 특정 데이터를 넣는 것 (어디에? = 맨 뒤에!)
* **insert와 노드 구성의 차이점**
  * 노드 구성 : 앞 노드를 연결하는 주소값을 설정해줘야 한다. 
  * insert : 데이터를 넣더라도 새로운 노드를 맨끝에 놓았을 때 기존의 노드가 가리키는 것 뿐만 아니라, 맨 끝 노드가 앞 노드를 가리키게 끔 해야한다. 
    * 맨 끝 노드 값을 tail 이기에 그 값을 업데이트 해야함도 잊지 말 것 
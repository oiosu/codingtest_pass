### 06. Tree 트리 

* **Node와 Branch를 이용해서 사이클을 이루지 않도록 구성한 데이터 구조** 
* 어디에 사용? 
  * **트리 중 이진트리의 형태의 구조로, 탐색(검색)알고리즘 구현을 위해 많이 사용된다.** 

![image-20220910172317131](C:\Users\LGD\AppData\Roaming\Typora\typora-user-images\image-20220910172317131.png)

* **Node**: 트리에서 데이터를 저장하는 기본 요소 (데이터와 다른 연결된 노드에 대한 Branch 정보 포함)

* **Root Node**: 트리 맨 위에 있는 노드

* **Level**: 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄

* **Parent Node**: 어떤 노드의 다음 레벨에 연결된 노드

* **Child Node**: 어떤 노드의 상위 레벨에 연결된 노드

* **Leaf Node** (Terminal Node): Child Node가 하나도 없는 노드

* **Sibling (Brother Node):** 동일한 Parent Node를 가진 노드

* **Depth**: 트리에서 Node가 가질 수 있는 최대 Level



---



#### ◼트리 장단점 

|            장점            |                             단점                             |
| :------------------------: | :----------------------------------------------------------: |
|     데이터 검색(탐색)      | 평균 시간 복잡도는 *𝑂*(*𝑙**𝑜**𝑔*) 이지만, 이는 트리가 균형잡혀 있을 때의 평균 시간복잡도이다. |
| 탐색 속도를 개선할 수 있음 | 최악의 경우는 링크드 리스트등과 동일한 성능을 보여줌 ( 𝑂 (𝑛) ) |





#### ✍ 필기내용 



* **노드 클래스 만들기**

  ```python
  class Node:
      def __init__(self, value):
          self.value = value
          self.left = None
          self.right = None
  ```



* **이진 탐색 데이터 넣기 **

![image-20220910173249393](C:\Users\LGD\AppData\Roaming\Typora\typora-user-images\image-20220910173249393.png)

```python
if value < self.current_node.value
```



* **이진 탐색 트리 탐색**

```python
def search(self, value)
```

> search 특정 데이터가 있는지 없는지 확인하기 위해!



* **이진 탐색 트리 삭제**
  * 매우 복잡하므로, 경우를 나누어서 이해하는 것이 좋다 (쪼개어서 생각하기)

1. **leaf node 삭제 : 삭제 후 None 으로 다시 설정** 
2. **child node 가 하나인 node 삭제** 

3. **child node 가 2개인 node 삭제 **  (삭제할 node의 오른쪽 중 가장 작은 값을 삭제할 node 의 parent가 node가 가리키도록 한다.)



![image-20220910182044807](C:\Users\LGD\AppData\Roaming\Typora\typora-user-images\image-20220910182044807.png)


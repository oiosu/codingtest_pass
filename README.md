
### ✔ 코딩테스트 대비 자료구조 및 알고리즘 문제 TIL

#### 📌 자료구조 
> Array 배열, Queue 큐, Stack 스택, Linked List 링크드 리스트, Hash 해쉬, Tree 트리, Heap 힙

---

#### [1. Array 배열](https://github.com/oiosu/codingtest_pass/blob/main/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_fastcampus/01_Array_%EB%B0%B0%EC%97%B4.md)

* **데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조** 
* **파이썬에서는 리스트 타입이 배열 기능을 제공**
* **같은 종류의 데이터를 효율적으로 관리하기 위해  사용**
* **같은 종류의 데이터를 순차적으로 저장**

![image](https://user-images.githubusercontent.com/99783474/189482276-b142200b-67f6-43c6-bcd6-68cd994a2dec.png)

#### 💡 [Array BAJ TIL](https://github.com/oiosu/codingtest_pass/tree/main/%EB%B0%B1%EC%A4%80_%EB%8B%A8%EA%B3%84%EB%B3%84/11_%EC%A0%95%EB%A0%AC)
> 2750 2751 10989 25305 2108 1427 11650 11651 1181 10814 18870

---

#### [2. Queue 큐](https://github.com/oiosu/codingtest_pass/blob/main/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_fastcampus/02_Queue_%ED%81%90.md)

* **가장 먼저 넣은 데이터를 먼저 꺼낼 수 있는 구조**
* **놀이공원서 가장 먼저 줄을 선 사람이 제일 먼저 입장하는 것과 동일**
* **FIFO 또는 LILO 방식으로 스택과 꺼내는 순서가 반대**
* **Enqueue : 큐에 데이터를 넣는 기능** **(= put)**
* **Dequeue: 큐에서 데이터를 꺼내는 기능** **(=get)**

![image](https://user-images.githubusercontent.com/99783474/189483174-b1424a82-12a4-413c-86a0-a8b5444e2871.png)
![image](https://user-images.githubusercontent.com/99783474/189483200-744391aa-f2c7-439e-9e51-beab67b74235.png)

#### 💡 [Queue BAJ TIL](https://github.com/oiosu/codingtest_pass/tree/main/%EB%B0%B1%EC%A4%80_%EB%8B%A8%EA%B3%84%EB%B3%84/6.%20%ED%81%90%20%26%20%EB%8D%B1)
> 18258 2164 11866 1966 10866 1021 5430

---

#### [3. Stack 스택](https://github.com/oiosu/codingtest_pass/blob/main/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_fastcampus/03_Stack_%EC%8A%A4%ED%83%9D.md)

* **데이터를 제한적으로 접근할 수 있는 구조 (한쪽 끝에서만 자료를 넣거나 뺼 수 있는 구조 )**

* **가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조** **(큐 FIFO vs 스택 LIFO)**
* **대표적 활용 : 컴퓨터 내부의 프로세스 구조의 함수 동작 방식**
* **push() : 데이터를 스택에 넣기** **pop() : 데이터를 스택에서 꺼내기**

![image](https://user-images.githubusercontent.com/99783474/189484884-f978e72c-0de8-4c1d-8eec-544404452ffc.png)

![image](https://user-images.githubusercontent.com/99783474/189484774-b568e568-87a9-4d18-8737-549de07d6d25.png)

#### 💡 [Stack BAJ TIL](https://github.com/oiosu/codingtest_pass/tree/main/%EB%B0%B1%EC%A4%80_%EB%8B%A8%EA%B3%84%EB%B3%84/7.%EC%8A%A4%ED%83%9D)
> 10828 10773 9012 4949 1874 17298

---

#### [4. Linked List 링크드 리스트 ](https://github.com/oiosu/codingtest_pass/blob/main/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_fastcampus/04_Linked%20List_%EB%A7%81%ED%81%AC%EB%93%9C%20%EB%A6%AC%EB%93%9C%EC%8A%A4.md)

![image](https://user-images.githubusercontent.com/99783474/189487198-1c353f00-130a-43c4-9087-03714af15953.png)
* **Linked List VS Array**
  * 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조 
  * 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조 
  * C언어는 주요한 데이터 구조이지만 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원


![image](https://user-images.githubusercontent.com/99783474/189487231-71e053b7-b6a4-4bc1-a7fe-c9e2d53e83aa.png)




* **NODE** : 데이터 저장단위 (데이터 값, 포인터)로 구성 (**구현 시 파이썬 객체지향 문법 이해 필요**)
* **Pointer** : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간 


#### ◼ 링크드 리스트의 장단점 

|                           장점                            |                 단점 _ 일반적인 스택 구현 시                 |
| :-------------------------------------------------------: | :----------------------------------------------------------: |
|        미리 데이터 공간을 미리 할당하지 않아도 됨         | 연결을 위한 별도 데이터 공간이 필요하므로, 저장 공간 효율이 높지 않음 |
| (반면, 배열은 미리 데이터 공간을 할당해야하는 점이 있다.) |    연결 정보를 찾는 시간이 필요하므로 접근 속도가 느리다.    |
|                             -                             | 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요 |


---

#### [5. Hash 해쉬 ](https://github.com/oiosu/codingtest_pass/blob/main/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_fastcampus/05_%20Hash_%ED%95%B4%EC%89%AC.md)

| **해쉬 Hash**                  | 임의 값을 고정 길이로 변환하는 것                            |
| :----------------------------- | :----------------------------------------------------------- |
| **해쉬 테이블 Hash Table**     | **키 값의 연산에 의해 직접 접근이 가능한 데이터 구조**       |
| **해싱 함수 Hashing Function** | **Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수** |
| **해쉬 값 Hash Vale**          | **Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있음** |
| **슬롯 Slot**                  | **한 개의 데이터를 저장할 수 있는 공간**                     |


![image](https://user-images.githubusercontent.com/99783474/189487302-da7daebe-c251-436c-91b3-bf44cd2d21c9.png)


---

#### [6. Tree 트리 ](https://github.com/oiosu/codingtest_pass/blob/main/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_fastcampus/06_Tree_%ED%8A%B8%EB%A6%AC.md)


* **Node와 Branch를 이용해서 사이클을 이루지 않도록 구성한 데이터 구조** 
* 어디에 사용? 
  * **트리 중 이진트리의 형태의 구조로, 탐색(검색)알고리즘 구현을 위해 많이 사용된다.** 


![image](https://user-images.githubusercontent.com/99783474/189487351-3a33661c-a394-47fd-8aa1-941cd846f7fd.png)

* **Node**: 트리에서 데이터를 저장하는 기본 요소 (데이터와 다른 연결된 노드에 대한 Branch 정보 포함)

* **Root Node**: 트리 맨 위에 있는 노드

* **Level**: 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄

* **Parent Node**: 어떤 노드의 다음 레벨에 연결된 노드

* **Child Node**: 어떤 노드의 상위 레벨에 연결된 노드

* **Leaf Node** (Terminal Node): Child Node가 하나도 없는 노드

* **Sibling (Brother Node):** 동일한 Parent Node를 가진 노드

* **Depth**: 트리에서 Node가 가질 수 있는 최대 Level


---

#### [7. Heap 힙 ](https://github.com/oiosu/codingtest_pass/blob/main/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0_fastcampus/07_Heap_%ED%9E%99.md)


* **데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리 (complete binary tree)**
* **완전 이진 트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리**
* 힙은 최대값을 구하기 위한 구조 **(최대 힙, Max Heap) 와, 최소값을 구하기 위한 구조 (최소 힙, Min Heap)** 로 분류할 수 있음

* 힙은 다음과 같이 두 가지 조건을 가지고 있는 자료구조
  * 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
  * 완전 이진 트리 형태를 가짐
* **힙은 완전 이진 트리이므로, 삽입할 노드는 기본적으로 왼쪽 최하단부 노드부터 채워지는 형태로 삽입**



#### ◼ 힙을 사용해야 하는 이유 

* **배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n)이 걸림**
* **이에 반해, 힙에 데이터를 넣고 최대값과 최소값을 찾으면 O(log) 걸림**
* **우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료 구노 및 알고리즘 구현등에 활용됨**



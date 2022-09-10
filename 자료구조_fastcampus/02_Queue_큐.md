### 02. Queue 큐 

![image-20220910120952218](C:\Users\LGD\AppData\Roaming\Typora\typora-user-images\image-20220910120952218.png)

* **가장 먼저 넣은 데이터를 먼저 꺼낼 수 있는 구조**
* **놀이공원서 가장 먼저 줄을 선 사람이 제일 먼저 입장하는 것과 동일**
* **FIFO 또는 LILO 방식으로 스택과 꺼내는 순서가 반대**
* **Enqueue : 큐에 데이터를 넣는 기능** **(= put)**
* **Dequeue: 큐에서 데이터를 꺼내는 기능** **(=get)**

---

![image-20220910123544870](C:\Users\LGD\AppData\Roaming\Typora\typora-user-images\image-20220910123544870.png)

---



#### ◼  Queue 라이브러리 활용 

* **queue 라이브러리 다양한 큐 구조로 3가지 제공**
  * **Queue(), LifoQueue(), PriorityQueue()**
    * Queue() 가장 일밙거인 큐 자료 구조 
    * LifoQueue() 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조)
    * PriorityQueue() 데이터마다 우선순위를 넣어, 우선순위가 높은 순으로 데이터 출력 



#### ◼ import queue

```python
import queue
data_queue = queue.Queue()
```



#### ◼ LifoQueue()

```python
import queue
data_queue = queue.LifoQueue()
```



#### ◼  PriorityQueue()

```python
import queue
data_queue = queue.PriorityQueue()
```



---

#### 

* **큐가 언제 많이 사용할까?**

> 멀티 캐스팅을 위한 프로세스 스케줄링 방식을 구현하기 위해 (wit 운영체제와 함께 알아두기)

> [참고글1](https://velog.io/@anjaekk/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EB%A9%80%ED%8B%B0%EC%BA%90%EC%8A%A4%ED%8C%85)  [참고글2](https://m.blog.naver.com/PostView.nhn?blogId=twers&logNo=50118680544&proxyReferer=https:%2F%2Fwww.google.com%2F)

**(1) 유니캐스팅**: 하나의 송신자, 하나의 수신자
**(2) 브로드캐스팅**: 하나의 송신자, 송신자 제외 모두 수신자
**(3) 멀티캐스팅**: 하나의 송신자, 특정 그룹에 속한 다수의 수신자


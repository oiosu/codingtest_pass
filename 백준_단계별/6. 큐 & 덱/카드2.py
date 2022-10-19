<<<<<<< HEAD
# 제일 마지막에 남게 되는 카드를 구하는 프로그램

# 시간 초과 코드 
N = int(input())
L = list(range(1,N+1))


while (len(L)>1):
    L.pop(0)
    temp = L.pop(0)
    L.append(temp)


print(L.pop(0))


# 다른 방법 코드 _ 성공
from collections import deque
 
n = int(input())
queue = deque()
 
for i in range(1,n+1):
    queue.append(i)
 
while True:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
=======
# 제일 마지막에 남게 되는 카드를 구하는 프로그램

# 시간 초과 코드 
N = int(input())
L = list(range(1,N+1))


while (len(L)>1):
    L.pop(0)
    temp = L.pop(0)
    L.append(temp)


print(L.pop(0))


# 다른 방법 코드 _ 성공
from collections import deque
 
n = int(input())
queue = deque()
 
for i in range(1,n+1):
    queue.append(i)
 
while True:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
>>>>>>> ffba77d72193687ce75e356a6d29096d959d5789
    queue.append(queue.popleft())
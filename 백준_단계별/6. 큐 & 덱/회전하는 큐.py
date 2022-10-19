<<<<<<< HEAD
# 큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. 
# (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 
# 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

from collections import deque
 
n , m = map(int, input().split())
 
queue = deque([i for i in range(1, n+1)])
 
arr = list(map(int, input().split()))
 
cnt = 0
 
for i in arr:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) <= len(queue) // 2:
                queue.rotate(-1)
                cnt += 1
            else:
                queue.rotate(1)
                cnt += 1
=======
# 큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. 
# (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 
# 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

from collections import deque
 
n , m = map(int, input().split())
 
queue = deque([i for i in range(1, n+1)])
 
arr = list(map(int, input().split()))
 
cnt = 0
 
for i in arr:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) <= len(queue) // 2:
                queue.rotate(-1)
                cnt += 1
            else:
                queue.rotate(1)
                cnt += 1
>>>>>>> ffba77d72193687ce75e356a6d29096d959d5789
print(cnt)
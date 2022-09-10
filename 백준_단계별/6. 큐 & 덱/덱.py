# 단순하게 생각해보기 복잡하면 코드가 작성이 안됨 

from collections import deque 
import sys

n=int(sys.stdin.readline())
dq=deque()
for _ in range(n):
  order=list(sys.stdin.readline().split())

  if order[0]=='push_front':
    dq.appendleft(order[1])

  elif order[0]=='push_back':
    dq.append(order[1])

  elif order[0]=='pop_front':
    if dq:
      x=dq.popleft()
      print(x)
    else:
      print(-1)

  elif order[0]=='pop_back':
    if dq:
      x=dq.pop()
      print(x)
    else:
      print(-1)

  elif order[0]=='size':
    print(len(dq))

  elif order[0]=='empty':
    if len(dq)==0:
      print(1)
    else:
      print(0)

  elif order[0]=='front':
    if dq:
      print(dq[0])
    else:
      print(-1)

  elif order[0]=='back':
    if dq:
      print(dq[-1])
    else:
      print(-1)

  else:
    print('예외')
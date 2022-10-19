<<<<<<< HEAD
# 입력으로 주어지는 명령을 처리하는 프로그램
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
sys.stdin = open(r"C:\Users\LGD\Desktop\코딩테스트 합격\백준_단계별\6. 큐 & 덱\큐2.txt", "r", encoding = 'utf-8')


# 런타임 에러 
testCase = int(input())
queue = []
cnt = 0
for i in range(testCase):
    comm = input().strip()
    if comm.split()[0] =='push':
        queue.append(int(comm.split()[1]))
    elif comm.split()[0]=='pop':
        if len(queue)-cnt ==0:
            print(-1)
        else:
            print(queue[cnt])
            cnt += 1

    elif comm.split()[0]=='size':
        print(len(queue)-cnt)
    elif comm.split()[0] =='empty':
        if len(queue)-cnt ==0:
            print(1)
        else:
            print(0)
    elif comm.split()[0]=='front':
        if len(queue)-cnt ==0:
            print(-1)
        else:
            print(queue[cnt])
            
    elif comm.split()[0]=='back':
        if len(queue)-cnt==0:
            print(-1)
        else:
            print(queue[-1])



# 두번째 방법 _ 성공 
import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for i in range(N):
    command = sys.stdin.readline().split()
    #print(command)

    if command[0] == "push":
        queue.append(command[1])

    elif command[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    
    elif command[0] == "size":
        print(len(queue))

    elif(command[0] == "empty"):
        if not queue:
            print(1)
        else:
            print(0)
    
    elif(command[0] == "front"):
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    else:
        if not queue:
            print(-1)
        else:
=======
# 입력으로 주어지는 명령을 처리하는 프로그램
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
sys.stdin = open(r"C:\Users\LGD\Desktop\코딩테스트 합격\백준_단계별\6. 큐 & 덱\큐2.txt", "r", encoding = 'utf-8')


# 런타임 에러 
testCase = int(input())
queue = []
cnt = 0
for i in range(testCase):
    comm = input().strip()
    if comm.split()[0] =='push':
        queue.append(int(comm.split()[1]))
    elif comm.split()[0]=='pop':
        if len(queue)-cnt ==0:
            print(-1)
        else:
            print(queue[cnt])
            cnt += 1

    elif comm.split()[0]=='size':
        print(len(queue)-cnt)
    elif comm.split()[0] =='empty':
        if len(queue)-cnt ==0:
            print(1)
        else:
            print(0)
    elif comm.split()[0]=='front':
        if len(queue)-cnt ==0:
            print(-1)
        else:
            print(queue[cnt])
            
    elif comm.split()[0]=='back':
        if len(queue)-cnt==0:
            print(-1)
        else:
            print(queue[-1])



# 두번째 방법 _ 성공 
import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for i in range(N):
    command = sys.stdin.readline().split()
    #print(command)

    if command[0] == "push":
        queue.append(command[1])

    elif command[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    
    elif command[0] == "size":
        print(len(queue))

    elif(command[0] == "empty"):
        if not queue:
            print(1)
        else:
            print(0)
    
    elif(command[0] == "front"):
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    else:
        if not queue:
            print(-1)
        else:
>>>>>>> ffba77d72193687ce75e356a6d29096d959d5789
            print(queue[-1])
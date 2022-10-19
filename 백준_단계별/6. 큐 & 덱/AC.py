# 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성


import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
for i in range(n):
    a = input().strip()
    m = int(input())
    flag = 1
    arr = input().strip()
    dq = deque(arr[1:-1].split(','))
    if m == 0:
        dq = deque()
    R = 0
    for i in range(len(a)):
        if a[i] == 'R':
            R += 1
        elif a[i] == 'D':
            if len(dq) == 0:
                print('error')
                flag = 0
                break
            else:
                if R % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    if flag == 0:
        continue
    else:
        if R % 2 == 0:
            print('[' + ",".join(dq) + ']')
        else:
            dq.reverse()
            print('[' + ",".join(dq) + ']')

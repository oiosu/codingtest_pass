import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\AC.txt", "r", encoding="utf-8")

# 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력

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



# 입력 배열의 파싱 , 0번째 인덱스와 마지막 인덱스를 제외하면
# [1,2,3,4] = > 1,2,3,4 로 만들어지므로
# arr[1:-1] 로 하면 1,2,3,4 라는 문자열이 만들어진다.
# 여기서 split(',') 하면 ['1','2','3','4'] 가 만들어진다.
# R을 할 시에는 배열을 reverse 해준다.
# 하지만 n번의 연산이 필요하다.
# R의 최대 횟수 100,000 , 배열의 최대 크기 100 , 테스트케이스 100개
# 100 100,000 100 = 1,000,000,000 1억번의 시간이 대략 소요가 된다. 시간초과가 날수도 있기때문에
# R을 짝수번 했을경우에는 배열을 reverse시키지 않아도 괜찮다.
# 그래서 R이 나왔을 경우에는 카운트를 해줘서
# D가 나왔을때 R이 짝수일경우에는 popleft , 홀수일경우에는 pop 을 해주고
# 마지막에 R이 홀수일 경우에 배열을 reverse해서 출력해주면 된다.


# 배열의 크기가 0인 경우에 D(삭제)를 실행할 경우 error메세지를 출력한다.
# 데크의 크기가 0 인경우에 D를 실행할 경우 , 입력 배열의 개수가 0 인 경우
# 두가지 경우를 생각하면 된다.
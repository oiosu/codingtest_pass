# 총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력

# 아직도 조금 어렵다. 

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

cnt = [0] # 오큰수를 0번째 인덱스부터 확인한다.
res = [-1] * n

for i in range(1, n):

    # 오큰수가 있는지 확인한다.
    while cnt and a[cnt[-1]] < a[i]:
        # 오큰수이면 비교한 값을 팝하고 오큰수를 입력 받는다.
        # 위 과정을 오큰수 리스트가 사라질 때까지 한다.
        res[cnt.pop()] = a[i]

    # 오큰수를 비교할 인덱스를 추가한다.
    cnt.append(i)

print(*res)
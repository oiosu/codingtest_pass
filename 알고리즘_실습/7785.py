# 회사에 있는 사람 
# 상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다.
# 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 
# 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성
# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.

import sys

n = int(sys.stdin.readline())
temp = dict() # 딕셔너리 형

# 반복문을 통해 출입 기록울 확인한다.
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())

    # 출입을 했으면 딕셔너리로 받는다.
    if b == "enter":
        temp[a] = b
    # 퇴근을 했으면 삭제해준다.
    else:
        del temp[a]

# 사전 순의 역순으로 정렬한다.
temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)
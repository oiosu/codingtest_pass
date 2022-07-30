# 듣보잡
# 김진영이 듣도 못한 사람의 명단과, 
# 보도 못한 사람의 명단이 주어질 때, 
# 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성
# input : 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
# 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
# output : 듣보잡의 수와 그 명단을 사전순으로 출력



# 공통된 부분은 set의 교집합을 사용한다. 

N , M = map(int,input().split())
arr_1 = set()
arr_2 = set()

for _ in range(N):
    arr_1.add(input())
for _ in range(M):
    arr_2.add(input())

arr = sorted(list(arr_1 & arr_2))
print(len(arr))

for i in arr:
    print(i)
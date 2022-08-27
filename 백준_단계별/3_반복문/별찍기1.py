# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

# n = int(input())
# for i in range(1, n):
#     print('*' * i)


number = int(input())

for i in range(1, number+1):   # 1부터 n까지
    print('*' * i)
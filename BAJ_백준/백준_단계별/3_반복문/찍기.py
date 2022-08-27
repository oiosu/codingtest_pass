# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다
n = int(input())


#range는 첫째 인자로 초기값, 둘째 인자로 종료값, 마지막 인자로 증가값을 적용

for i in range(1, n+1):  # 1부터 n까지
    print(i)


# [print(i) for i in range(1, int(input())+1)]
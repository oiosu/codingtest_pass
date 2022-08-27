<<<<<<< HEAD
# x보다 작은 수 
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\알고리즘_실습\10871.txt", "r", encoding = 'utf-8')


# number = int(input())
# result =
# for i in range(number):
#     i < x
#     print(number)

N, X = map(int, input().split())
Numbers = list(map(int, input().split()))

for i in range(N):
    if Numbers[i] < X:
        print(Numbers[i], end=" ")
=======
# x보다 작은 수 
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오


>>>>>>> e68f871a777dd7aa2e5b17bfa3729cbb52d045c8

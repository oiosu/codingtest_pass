# import sys
# sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2019.txt", "r", encoding = 'utf-8')

# 오답
# N = int(input())
# for i in range(N+1):
#     N = (2**i, N)
#     print(N, end= " ")


N = int(input())
for i in range(N+1):
    print(2**i, end=" ")

#pass
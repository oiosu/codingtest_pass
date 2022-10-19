# 2019
# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력
# 주어질 숫자는 30을 넘지 않는다.

# import sys
# sys.stdin = open("2019.txt", "r", encoding='utf-8')

# result = int(input()) 

# for i in range(0, result+1):
#         print(2*result, end=" ")

#코드 출력하는 과정중에 UnicodeDecodeError 발생함 
#encoding = 'utf-8' 추가 작성하여 해결함
#16 16 16 16 16 16 16 16 16  이라고 출력됨 다른 방법으로 작성하기 


N = int(input())
for i in range(N+1):
    print(2**i, end=" ")

# 위와 같은 코드로 출력시 맞게 출력됨 pass
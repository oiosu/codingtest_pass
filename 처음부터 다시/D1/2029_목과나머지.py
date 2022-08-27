# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력

#import sys
#sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2029.txt", "r", encoding = 'utf-8')

result = int(input())
for i in range(1, result+1):
    a, b = map(int, input().split())

    print("#{} {} {}".format(i, a//b, a%b))


# 다른 풀이 참고하기!

# a 와 b를 입력받아 각 테스트 케이스 번호와 함께 a를 b로 나눈 몫과 나머지 값을 출력
# 형식에 맞추어 출력한다. 

# t = int(input())

# for i in range(1, t + 1) :
#     a, b = map(int, input().split())
#     print("#%d" % i, end=" ")
#     print(a // b, end=" ")
#     print(a % b)


# map 생각할떄마다 얼어붙지 말기
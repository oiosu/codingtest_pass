#두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성
#두 개의 자연수 a, b는 1부터 9까지의 자연수
#사칙연산 + , - , * , / 순서로 연산한 결과를 출력
#나누기 연산의 결과에서 소수점 이하의 숫자는 버린다.

#import sys
#sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\1938.txt", "r", encoding = 'utf-8')

a, b = map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)


# map을 생략하는 일이 자주 발생 주의하자!
# pass
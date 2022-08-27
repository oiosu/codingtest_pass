# 각 테스트 케이스마다 A+B를 출력

t = int(input())

for i in range(t):
    a, b = map(int, input().split())  # 순서 주의하기 
    print(a + b)
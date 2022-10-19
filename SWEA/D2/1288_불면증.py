# import sys
# sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D2\1288.txt", "r", encoding = 'utf-8')


#분명히 알았던 문제였는데..혼란 그자체 다시 생각해보는 힘을 기르자

result = int(input())

for i in range(1, result+1):
    N = input()     # N을 문자열 형태로 입력받기
    value = int(N)  # 정수형으로 변환된 값을 value에 할당
    data = [0] * 10 # 각 자리수의 번호를 세긴 횟수가 담겨질 리스트 정의
    while True:
        for j in range(len(N)):  
            data[int(N[j])] += 1
        if not data.count(0):     # 리스트의 요소들 중 0이 없을 경우 
            print('#%d %d' % (i, int(N)))
            break      # 반복문 종료 

        N = str(value + int(N))


# 0이 존재하는 경우 vlaue값과 현재의 n값을 더해 문자열로 변환하여 값을 출력?


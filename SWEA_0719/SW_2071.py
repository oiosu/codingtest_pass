#평균값 구하기
# import sys
# sys.stdin = open("SW_2071.txt", "r")

#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성
#(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

T = int(input())
for i in range(T) :
    nums = map(int,input().split())
    res = sum(n for n in nums)
    print( f"#{i+1} {round(res/10)}" )  
#거꾸로 출력하기
# import sys
# sys.stdin = open("SW_1545.txt", "r")

T = int(input())
for i in range(T, -1, -1):       #for문으로 범위설정
    print( i, end=' ' )
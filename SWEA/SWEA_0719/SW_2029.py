# import sys
# sys.stdin = open("SW_2029.txt", "r")

T = int(input())

for tc in range(1, T+1):               #for문으로 범위 설정 
    a, b = map(int, input().split())   

    print("#{} {} {}".format(tc, a//b, a%b))
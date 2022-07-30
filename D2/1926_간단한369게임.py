import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D2\1926.txt", "r", encoding = 'utf-8')


# 문제풀이 시 집중이 안되어서 계속 고민하다가 다른 풀이 참고함 

N = int(input()) #1부터 출력할 숫자의 범위
for num in range(1, N + 1):
    temp = num # 현재 숫자에서 (3,6,9)의 갯수를 구하기 위한 변수
    cnum = 0 # 현재 숫자에서 (3,6,9)의 갯수
    while temp > 0: # 현재 수에서 검사할 숫자가 남아있다면
        if temp % 10 in [3, 6, 9]: # 가장 오른쪽 자리 수가 (3,6,9)안에 있다면
            cnum += 1 # 갯수 증가
        temp //= 10 # 현재 수 / 10
    if cnum > 0: # (3,6,9)개수가 1개 이상이면
        print("-" * cnum, end=" ") #'-'를 갯수만큼 출력
    else:
        print(num, end=" ") #해당 수 출력
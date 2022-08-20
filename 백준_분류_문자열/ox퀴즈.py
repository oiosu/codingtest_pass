# OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\ox퀴즈.txt", "r", encoding="utf-8")

n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)
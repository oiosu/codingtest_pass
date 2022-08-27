# 단어를 열 개씩 끊어서 한 줄에 하나씩 출력
# 단어의 길이가 10의 배수가 아닌 경우에는 마지막 줄에는 10개 미만의 글자만 출력

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\열개끊어 출력.txt", "r", encoding="utf-8")

n = input() # n변수를 설정해서 문자열 값을 입력

# range(시작값, 종료값, step)
for i in range(0, len(n), 10):  # for문을 통해서 0부터 len(n)으로 n의 문자열의 길이까지 10씩 끊어서 i를 입력
    # 마지막으로 입력받은 문자열 n을 i부터 i에서 10더한 값만큼 끊어서 슬라이싱 해서 출력한다. 
    # a[시작값:원하는 종료값 +1]
    print(n[i:i+10])
import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\팰린드롬수.txt", "r", encoding="utf-8")

# 리스트 슬라이싱 

while True:
    n = input()

    if n == '0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')
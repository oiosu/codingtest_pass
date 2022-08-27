# 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\단어의개수.txt", "r", encoding="utf-8")

word = input().split()
print(len(word))
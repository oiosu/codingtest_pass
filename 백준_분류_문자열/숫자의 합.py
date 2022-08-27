# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\숫자의 합.txt", "r", encoding="utf-8")

n = input()
nums = input()
total = 0

for i in nums:
    total += int(i)
print(total)
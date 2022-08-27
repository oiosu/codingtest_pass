import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2050.txt", "r", encoding = 'utf-8')


for c in input():
    print( ord(c)-64, end=' ' )
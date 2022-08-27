import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2070.txt", "r", encoding = 'utf-8')

num = int(input())

for i in range(0, num):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a < b:
        print("#%d %s" %(i+1, '<'))
    elif a > b:
        print("#%d %s" %(i+1, '>'))
    else:
        print("#%d %s" %(i+1, '='))

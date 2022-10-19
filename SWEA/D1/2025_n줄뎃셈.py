#import sys
#sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2025.txt", "r", encoding = 'utf-8')

result = int(input())
sum = 0

for i in range(1, result+1):
    sum = sum + i

print(sum)
import math
import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2071.txt", "r", encoding = 'utf-8')


 
T = int(input())
for test_case in range(1, T + 1):
    sum = 0
    li = list(map(int, input().split()))
    for i in li :
        sum += i
    print("#{} {}".format(test_case, round(sum/len(li))))

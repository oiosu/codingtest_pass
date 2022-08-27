# N이 9 이고, 9개의 점수가 아래와 같이 주어질 경우,
# 85 72 38 80 69 65 68 96 22
# 69이 중간값이 된다.

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2063.txt", "r", encoding = 'utf-8')


n = int(input())
values = list(map(int, input().split()))
values.sort()
index_number = (n-1)//2
print("{}".format(values[index_number]))
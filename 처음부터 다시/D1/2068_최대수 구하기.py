import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2068.txt", "r", encoding = 'utf-8')


k = int(input())
for i in range(k):
    j = list(map(int, input().split()))
    max_num = j[0]
    for y in range(len(j)):
        if max_num <= j[y]:
            max_num=j[y]
        else:
            continue
    print("#%d" %(i+1), max_num)
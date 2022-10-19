# import sys
# sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D2\1976.txt", "r", encoding = 'utf-8')

# 으어어어어어어엉!!! 

T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h3 = h1 + h2
    m3 = m1 + m2
    if m3 >= 60:
        h3 += 1
        m3 -= 60
    if h3 > 12:
        h3 -= 12
    print('#{} {} {}'.format(tc, h3, m3))
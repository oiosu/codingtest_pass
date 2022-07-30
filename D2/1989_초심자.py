# import sys
# sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D2\1989.txt", "r", encoding = 'utf-8')

T = int(input())
for i in range(1, T+1):
    word = input()
    if word == word[::-1]:
        print('#{} {}'.format(i, 1))
    else:
        print('#{} {}'.format(i, 0))
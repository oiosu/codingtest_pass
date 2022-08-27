import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\명령프롬프트.txt", "r", encoding="utf-8")

n = int(input())
a = list(input())
a_len = len(a)
for i in range(n - 1):
    b = list(input())
    for j in range(a_len):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))
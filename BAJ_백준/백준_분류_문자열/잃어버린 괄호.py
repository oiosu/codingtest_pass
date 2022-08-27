# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\잃어버린 괄호.txt", "r", encoding="utf-8")

# 최초로 마이너스가 나오기 전까지 나오는 숫자는 모두 더할 수 밖에 없으며, 이후 마이너스가 나오는 순간 그 뒤에 있는 모든 수들을 
# 빼주면 된다. 

s = input().split('-')

sum = 0
for i in s[0].split('+'):
    sum += int(i)
for i in s[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)

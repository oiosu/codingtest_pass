# 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\괄호.txt", "r", encoding="utf-8")

T = int(input())

for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됬을경우 수행한다
        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")
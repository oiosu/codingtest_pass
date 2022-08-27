# 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\균형잡힌세상.txt", "r", encoding="utf-8")

while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')


# "."은 입력의 종료조건이다.
# stack 리스트를 만들어서 먼저 발생된 시작되는 괄호를 저장해주고,
# 짝이 맞는 괄호가 생기면 .pop으로 리스트를 비워준다.
# 짝이 맞지 않는 괄호가 생기면 stack 리스트를 그대로 둔다.
# stack의 리스트가 비어있으면 yes를 출력하고, 비어있지 않으면
# no를 출력한다.
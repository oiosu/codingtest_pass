# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력

# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split())
#     print(a + b)

import sys
 
inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
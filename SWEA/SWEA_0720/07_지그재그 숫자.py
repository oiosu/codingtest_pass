# 1986
# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

# import sys
# sys.stdin = open("1986.txt", "r", encoding='utf-8')

T = int(input())

for i in range(1, T+1):
    N = int(input())
    result = 0

    for i in range(1, N+1):
        if i % 2 == 0: #짝수
            result -= i
        else: #홀수
            result += i

    print('#%d %d' % (i, result))


# 코드 하나하나씩 잘 살펴보기_이해할때까지 풀어보기 
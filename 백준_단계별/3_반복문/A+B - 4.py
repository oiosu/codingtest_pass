# 각 테스트 케이스마다 A+B를 출력한다.
#  try - except 구문 설명
# 파이썬에서 구문 오류가 발생 할 때 해결할 수 있는 코드이다. 
# 프로그램 중에는 사용자가 무엇인가를 입력해야 하는 경우 에러가 발생할 가능성이 있다. 
# 숫자를 입력해야 하는데 문자를 입력한다던가 실수를 입력해야 하는데 정수를 입력하는 등이 그런 예이다.
# 백준 알고리즘 문제에서는 잘못 입력될 가능성이 없기 때문에 구문 오류에 대해 고려하지 않고 문제를 풀고 있지만 
# 여러 가지 에러로 인해 프로그램이 실행되지 않을 수가 있다. 이러한 에러가 발생할 여지가 있는 경우에 
# try - except 구문을 이용하면 에러가 발생돼도 프로그램이 멈추지 않고 계속 진행될 수 있도록 만들 수 있다.



# 이번 문제는 두 수로 이루어진 여러 개의 테스트 케이스를 입력받으면 두 수의 합을 출력하는 문제이다. 
# 테스트 케이스의 숫자가 주어지지 않기 때문에 while 반복문을 이용해서 문제를 풀었고 수가 입력되지 않아서 
# 에러가 발생하면 반복문을 끝낼 수 있도록 try - except 구문을 활용해서 문제를 풀었다. 

while 1:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# try:
#     while 1:
#         a , b = map(int, input().split())
#         print(a + b)
# except: 
#     exit()
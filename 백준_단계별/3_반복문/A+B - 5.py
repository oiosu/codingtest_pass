# 각 테스트 케이스마다 A+B를 출력

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break;
    else:
        print(a + b)


# 무한루프로 while문을 돌린다.
# a와 b를 int형으로 받아주고, 만약 a와 b둘다 0이면 break로 while문을 빠져나와 준다.
# a + b 값을 print 해준다.
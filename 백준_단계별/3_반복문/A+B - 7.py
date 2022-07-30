# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

# T = int(input())
# for i in range(T):
#     A, B = map(int, input().split())
#     print("Case #x:", A + B)


t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')
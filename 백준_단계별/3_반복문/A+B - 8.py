# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B


# T = int(input())
# for i in range(1, T+1):
#     print(f'Case #{i}: {a+b=c}')

t = int(input())

for x in range(1, t+1):  # 1부터 t까지
    a, b = map(int, input().split())
    print(f'Case #{x}: {a} + {b} = {a+b}')
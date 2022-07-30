# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
# 출력형식과 같게 N*1부터 N*9까지 출력한다.

n = int(input())

for i in range(1, 10):
    print(n, "*", i, "=", n*i)



# numbers = int(input())

# for i in range(1, 10):
#     print(numbers, "*", i, "=", numbers*i)
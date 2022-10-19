# 수 찾기 
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# 예제 
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# 출력
# 1
# 1
# 0
# 0
# 1

# 안에 X라는 정수가 존재한다면 1 아니면 0을 출력하는 프로그램 

# 4개의 변수 
N = 5
N_list = [4, 1, 5, 2, 3]
M = 5
M_list = [1, 3, 7, 9, 5]

# 반복문 
for item in M_list:
    if item in N_list:
        print(1)
    else:
        print(0)

# 위와 같은 코드로 간단하게 구현해 볼 수 있지만 우리는 시간복잡도도 생각해야 한다. 따라서 다음과 같이 이진탐색을 통해 코드를 작성한 것이다. 
# 면저 sort로 정렬해주고 
# 이진탐색 구현 방법을 통해 O(log n)으로 개선할 수 있다.


N_list.sort()
def binary_search(data, search):
    if len(data) == 0:
        return 0
    elif len(data) == 1:
        if data[0] == search:
            return 1
        else:
            return 0
    
    medium = len(data) // 2
    if search == data[medium]:
        return 1
    else:
        if search > data[medium]:
            return binary_search(data[medium+1:], search)
        else:
            return binary_search(data[:medium], search)
        
for item in M_list:
    print(binary_search(N_list, item))        
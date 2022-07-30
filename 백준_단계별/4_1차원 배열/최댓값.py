# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력
# 9개의 수를 for문으로 입력받는 코드

numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)
    
print(max(numbers))
print(numbers.index(max(numbers))+1)


# numbers = [int(input()) for _ in range(9)]

# print(max(numbers))
# print(numbers.index(max(numbers)) + 1)
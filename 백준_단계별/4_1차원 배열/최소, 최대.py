# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

cnt = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min: 
        min = i
print(min, max)
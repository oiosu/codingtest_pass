# 1065 한수
# 어떤 양의 정수 x의 각 자리가 등차수열을 이룬다면, 
# 그 수를 한수라고 한다. 
# 등차수열은 연속된 2개의 수의 차이가 일정한 수열을 말한다. 
# n이 주어졌을 때 1보다 크거나 같고 n보다 작거나 같은 하수의 개수를 출력 

numbers = int(input())
hansu = 0
for i in range(1, numbers + 1):  
    if i < 100:   #1~99 까지의 수는 모두 등차수열로 구분 
        hansu += 1  #만약 i 가 100보다 작다면 hansu에 +1를 한다. 
    else: 
        numbers1 = list(map(int, str(i)))  #map함수와 list를 사용하여 수를 하나씩 나눠준다.
        if numbers1[0] - numbers1[1] == numbers1[1] - numbers1[2]:
            # 첫번째 숫자와 두번째 숫자의 차와 두번째 숫자와 마지막 숫자의 차이가 같다면
            # 한수의 +1을 한다. 
            hansu += 1

print(hansu)
#1933
# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성

# 약수란 해당 수(input값 10)를 나누었을 때 0이 나오게 하는 수를 말한다. 
# 어떤 값으로 나누다 (%)

# import sys
# sys.stdin = open("1933.txt", "r")

number = int(input())  #number를 통해 정수 n을 입력한다. 

for i in range(1, number+1): #for문을 통해  범위만큼 반복하도록 한다. 
    if number % i == 0:   #만약 input된 수를 나우었을 때 0이된다면, (약수를 구하기)
        #줄 바꿈이 없이 띄어쓰기로 나열이 되기 때문에 다음과 같이 출력한다.       
        print(i, end =" ")  

# 코드를 작성 후 제출하는 과정에서
# taberror: inconsistent use of tabs and spaces in indentation 오류 발생 
# 이는 스페이스 or 탭 공간? 사용유무? 에 대한 오류 
# Memory error occured 라는 에러도 발생
# 위 코드 모두 코드를 다시 작성하고 제출하기 전 플랫폼에 맞게 다시 검토 후 pass
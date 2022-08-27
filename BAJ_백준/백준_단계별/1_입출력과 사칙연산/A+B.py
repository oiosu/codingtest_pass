# 첫째 줄에 A+B를 출력한다.

# 입력되는 문자를 input()함수로 입력받고 split()함수로 나누어 A,B 변수에 저장
# A, B = input().split()	

# # int() 함수로 A와 B를 정수로 변환 하고 두수의 합을 출력
# print(int(A)+int(B))


# 위코드 : 런타임 에러 2회, 컴파일 에러 1회 발생 
# 위와 같은 코드보다 다음과 같은 코드로 작성하기 
A, B = map(int, input().split())
print(A + B)
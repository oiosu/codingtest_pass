# 두 수 비교하기 
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

A, B = map(int, input().split()) 

if A > B:   # 만약 A가 B 보다 크다면
	print(">") # > 라는 기호를 출력해주세요
elif A < B:  # B가 A 보다 크다면 
	print("<") # < 라는 기호를 출력해주세요. 
elif A == B:  # A와 B가 같다면 
	print("==")  # == 라는 기호를 출력해주세요. 

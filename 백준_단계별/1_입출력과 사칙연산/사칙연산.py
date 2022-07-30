# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
print(A // B) # 기호 주의하기 
print(A % B)
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

# 컴파일 에러 코드 
# A, B, C = map(int, input().split())

# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A×B)%C)
# print(((A%C) × (B%C))%C)

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
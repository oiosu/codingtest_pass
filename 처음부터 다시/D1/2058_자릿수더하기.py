import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2058.txt", "r", encoding = 'utf-8')

result = 0 
number = int(input(""))

while True:
    if number == 0:
        break
    result += number % 10
    number = number // 10
print(result)


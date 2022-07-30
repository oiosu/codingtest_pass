# o, x 퀴즈
n = int(input())

for i in range(n):
    count = 0 
    sum = 0

a = list(input())

for i in a : 
    if i == '0':
        count += 1
        sum = sum + count
    else:
        count = 0
print(sum)
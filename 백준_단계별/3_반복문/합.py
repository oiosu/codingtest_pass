# 1부터 n까지 합을 출력한다.

n = int(input())
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)
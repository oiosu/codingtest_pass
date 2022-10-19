n = int(input())
Minute = list(map(int, input().split()))
Minute.sort()
 
result = 0
 
for i in range(n):
    for j in range(i+1):
        result += Minute[j]
 
print(result)
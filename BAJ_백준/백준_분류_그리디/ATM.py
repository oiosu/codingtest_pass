<<<<<<< HEAD
n = int(input())
Minute = list(map(int, input().split()))
Minute.sort()
 
result = 0
 
for i in range(n):
    for j in range(i+1):
        result += Minute[j]
 
=======
n = int(input())
Minute = list(map(int, input().split()))
Minute.sort()
 
result = 0
 
for i in range(n):
    for j in range(i+1):
        result += Minute[j]
 
>>>>>>> ffba77d72193687ce75e356a6d29096d959d5789
print(result)
# 슈퍼마리오 
# 꼭 다시 풀어볼 것 

arr = []

for i in range(10):
    arr.append(int(input()))

arr2 = arr.copy()

for i in range(1,10):
    arr2[i] += arr2[i-1]
    
minNum, minNumIdx = 100, 0

for j in range(10):
    if abs(arr2[j] - 100) <= minNum:
        minNumIdx = j
        minNum = abs(arr2[j] - 100)
    else: 
        break
        
print(arr2[minNumIdx])

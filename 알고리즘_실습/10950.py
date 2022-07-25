numbers = int(input())

for i in range(numbers): #for문을 사용
    A, B = map(int, input().split()) #map 사용
    print(A + B)

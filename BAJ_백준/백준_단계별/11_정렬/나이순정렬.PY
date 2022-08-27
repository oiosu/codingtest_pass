n = int(input())
li = []
for _ in range(n):
    age, name = input().split()
    li.append([int(age), name])

li.sort(key=lambda x:int(x[0]))
for i in li:
    print(i[0], i[1])
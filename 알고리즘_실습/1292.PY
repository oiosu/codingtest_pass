# 쉽게 푸는 문제 
# 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 
# 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것
# 첫 줄에 구간에 속하는 숫자의 합을 출력한다.

# 3 3 3 3 7 7 7 7 7 7 7 

x, y = map(int, input().split())
a = []
for i in range(y+1) :
    for j in range(i):
        if len(a) == y :
            break
        a.append(i)
print(sum(a[x-1:y]))
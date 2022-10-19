# 재민이가 최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 231-1보다 작거나 같은 정수이다.

#리스트를 이용하여 스택 구현 
k = int(input())
 
li = []
for _ in range(k):
    n = int(input())
    if n==0:
        li.pop()
    else:
        li.append(n)
print(sum(li))
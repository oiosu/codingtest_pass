# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력

n = []
for _ in range(10):
    A = int(input())
    B = A % 42
    n.append(B)

S = set(n)
print(len(S))
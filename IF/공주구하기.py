import sys
from collections import deque

sys.stdin = open(r"C:\Users\LGD\Desktop\코딩테스트 합격\IF\공주구하기.txt", "r", encoding="utf-8")

# n, k = map(int, input().split())
# dq = list(range(1, n + 1))
# # print(dq)

# dq = deque(dq)

# while dq:
#     for _ in range(k - 1):
#         cur = dq.popleft()
#         dq.append(cur)
#     dq.popleft()
#     if len(dq) == 1:
#             print(dq[0])
#             dq.popleft()


a, b = map(int, input().split())
result = a * b

print(result)


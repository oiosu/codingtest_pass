from re import I
from scipy.misc import central_diff_weights


n, m = map(int, input().split())
res = [0] * n
ch = [0] * (n + 1)
cnt = 0
# DFS(0)


def DFS(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L + 1)
                ch[i] = 0
        print(cnt)

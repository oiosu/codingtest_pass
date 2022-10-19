<<<<<<< HEAD
#첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
par = [-1]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(n):
    for i in tree[n]:
        if par[i] == -1:
            par[i] = n
            dfs(i)
            
dfs(1)
for i in range(2,n+1):
=======
#첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
par = [-1]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(n):
    for i in tree[n]:
        if par[i] == -1:
            par[i] = n
            dfs(i)
            
dfs(1)
for i in range(2,n+1):
>>>>>>> ffba77d72193687ce75e356a6d29096d959d5789
    print(par[i])
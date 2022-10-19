def DFS(L, s, sum):
    global cnt 
    if L == k:
        if sum % m == 0:
            cnt +=1
    else: 
        for i in range(s, n):
            # DFS(L+1, i+1, sum+a[i])
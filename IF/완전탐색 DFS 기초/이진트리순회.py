# 전위순회
def DFS(v):
    if v > 7:
        return
    else:
        print(v)
        DFS(v * 2)
        DFS(v * 2 + 1)


# 중위순회
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v * 2)
        print(v, end=" ")
        DFS(v * 2 + 1)


# 후위순회 (보통 후위순회 많이 사용 _ 병합 정렬)
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v * 2)
        DFS(v * 2 + 1)
        print(v, end=" ")


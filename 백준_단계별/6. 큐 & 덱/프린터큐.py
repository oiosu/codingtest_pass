# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력


# 런타임 에러 코드 
case = int(input())

for i in range(case):
    n, m = map(int, input().split())
    queue = list(map(int, input().split))
    cnt = 0     #m이 큐를 몇번째 빠져나갔는지 저장할 cnt 


    while(m != -1): # m이 -1이라면 큐를 빠져 나온 것
        if queue[0] == max(queue): # 큐의 맨 앞이 제일 크면
            del queue[0]  # 삭제해주고 
            m -= 1 # m이 한 칸 앞을 가리키게 한다. 
            cnt += 1 # 큐에서 하나 빠져 나갔으니 +1
        else:        # 맨앞이 제일 크지 않으면 
            queue.append(queue[0]) # 뒤에 추가해주고 
            del queue[0]  # 맨앞은 지워준다. 
            if m == 0:  # m이 0이었다면 
                m = len(queue) - 1   # 해당 자리에 있던 수가 뒤로 갔으니 m 도 맨 뒤를 가리키게 한다. 
            else:  # m이 0이 아니였다면 
                m -= 1 # 한칸 앞을 가리키게 한다. 


# 성공한 코드 
T = int(input())
 
for _ in range(T):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    index = [i for i in range(n)]
    index[m] = 'target'    # 내가 찾고 싶은 index
    cnt = 0
 
    while priority:
        if priority[0] == max(priority):    # 나머지 문서들보다 중요도가 더 높은 문서가 없다면
            cnt += 1
            if index[0] == 'target':
                print(cnt)
                break
            priority.pop(0)
            index.pop(0)
        else:
            priority.append(priority.pop(0))
            index.append(index.pop(0))
N = int(input())
way = list(map(int, input().split()))

temp = 0 # 높이를 임시로 저장할 변수 
ans = [] # 오르막길의 높이를 저장할 리스트 

# for문을 돌면서 앞길의 높이와 뒷길의 높이를 비교하여 
# 오르막길이라면 temp += (뒷길 높이 - 앞길 높이) 해준다. 
# i == N-1 이고 오르막길이라면 ans에 추가가 되지 않으므로 if 문을 만들기 
# 만약 오르막길이 아니라면 ans 에 temp를 더해주고 temp를 0으로 초기화 해준다. 

for i in range(1, N):
    if way[i] > way [i-1]:
        temp += way[i] - way[i-1]
        if i == N-1:
            ans.append(temp)
    else: 
        ans.append(temp)
        temp = 0
print(max(ans))   # 최종적으로 오르막길의 높이가 저장된 ans의 max 값을 출력한다. 
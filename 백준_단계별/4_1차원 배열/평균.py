# 첫째 줄에 새로운 평균을 출력한다. 
# 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답

subject = int(input())
scores = list(map(int, input().split()))
M = max(scores)

for i in range(subject):
    scores[i] = scores[i]/M*100

print(sum(scores)/subject)
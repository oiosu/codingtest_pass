# 프로그래머스 
# 음양더하기 

# for문으로 absolutes의 길이까지 signs[i]인 경우 answer에 absolutes[i]를 더한다.
# False인 경우 answer에 absolutes[i]를 뺀다.

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)): 
        if signs[i]: #signs[i]인 경우 true
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
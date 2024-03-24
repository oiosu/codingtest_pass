# 문제설명
# A반 학생들은 시험이 끝난 뒤 성적이 나오기 전 자기 시험지를 가채점 해봄 
# 이후 선생님이 실제 성적을 불러 줄 때 가채점한 점수와 성적이 다른 학생들이 있어 선생님께 문의

# 성적을 문의하려는 학생들의 담긴 정수 리스트 numbers
# 가채점한 점수가 성적을 문의하려는 학생 순서대로 담긴 정수 리스트 our_score
# 실제 성적이 번호 순서대로 담긴 정수 리스트 score_list

# 주어진  solution 함수는 가채점한 점수가 실제 성적과 동일하다면 Same 
# 다르다면 Different를 순서대로 리스트에 담아 return 하는 함수 

def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        # if numbers[our_score[i]] == score_list[i]:
        if numbers[our_score[i]] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
            
    return answer
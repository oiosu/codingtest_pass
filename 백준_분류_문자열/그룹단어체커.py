# ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\그룹단어체커.txt", "r", encoding="utf-8")

n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0

for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
    if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
        new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
    if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
        error += 1  # error에 1씩 증가.
    if error == 0:
                group_word += 1  # error가 0이면 그룹단어
print(group_word)



# n = int(input())

# result = n
# for i in range(n) :
#   value = input()
#   for j in range(len(value) - 1) :
#     if value[j] == value[j + 1] :
#       pass
#     elif value[j] in value[j+1:] :
#       result -= 1
#       break

# print(result)
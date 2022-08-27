# 알파벳의 각 요소가 S에 존재하면 그때 S에서의 위치를 반환하기 위해 index 사용
# 그리고 예제출력을 보면 각 위치를 한칸씩 띄어서 반환하기 때문에 출력이후 한칸을 띄우는 end=' ' 을 사용.
# 알파벳을 나열하는 것 대신 a는 아스키코드 값으로 97로 이걸 기준으로 삼아서 수의 차이를 이용해 문제를 해결함
# baekjoon

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\알파벳찾기.txt", "r", encoding="utf-8")

S = input()
check = [-1]*26
 
for i in range(len(S)):
    if check[ord(S[i])-97] != -1:
        continue
    else:
        check[ord(S[i])-97] = i
        
for i in range(26):
    print(check[i], end=' ')
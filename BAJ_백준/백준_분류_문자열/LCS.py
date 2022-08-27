import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\LCS.txt", "r", encoding="utf-8")

# 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제

import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
l1, l2 = len(word1), len(word2)
cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1
print(max(cache))

# cnt를 누적 변수로 사용한다.
# 누적 변수의 값이 캐시값보다 작으면 교체한다.
# 글자가 같은 경우 누적 변수에서 1을 더한다.
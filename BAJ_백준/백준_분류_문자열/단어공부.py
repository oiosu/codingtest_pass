# 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\단어공부.txt", "r", encoding="utf-8")

word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])


# upper메소드의 사용법 대하여 알 수 있었다.
# count메소드의 사용법에 대해 알 수 있었다.
# index, max 함수에 대해 알 수 있었다.
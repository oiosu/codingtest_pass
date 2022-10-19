# The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.
# 위와 같은 문자열이 입력으로 주어졌을 때, 출력은 다음과 같다.
# THE_HEADLINE_IS_THE_TEXT_INDICATING_THE_NATURE_OF_THE_ARTICLE_BELOW_IT.


import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2047.txt", "r", encoding = 'utf-8')

sentence = input()
sentence = sentence.upper()
print(sentence)

# 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\알파벳개수.txt", "r", encoding="utf-8")

import sys

sentence = sys.stdin.readline().rstrip()

alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
            'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
            'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
            'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
            'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

for s in sentence:  #알파벳 개수 세서 value값에 저장하기
    alphabet[s] += 1

for n in alphabet.values():  #결과출력
    print(n, end=' ')




# import sys
# input = sys.stdin.readline
# text_lst = list(input())
# alphabet_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for i in range(len(alphabet_lst)) :
#     print(text_lst.count(alphabet_lst[i]),end=" ")
# 입력받은 그대로 출력

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\그대로출력.txt", "r", encoding="utf-8")

while True:
    try:
        print(input())
    except EOFError:
        break


# 예외 처리 구문 : try~ except~문
# try:
#    (예외가 발생할 수도 있는 코드)
# except:
#    (예외가 발생했을 경우 실행되는 코드)


# EOFError
# : 입력이 끝남(End Of File) 에러
# 데이터가 없어 더 이상 값을 읽을 수 없을 때 발생하는 에러
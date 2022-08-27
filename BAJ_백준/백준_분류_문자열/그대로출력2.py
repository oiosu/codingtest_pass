import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\그대로출력2.txt", "r", encoding="utf-8")


# try except문을 사용하여 예외처리를 해준다.
# * EOFError : EOF란 파일의 끝을 의미하며, 갑자기 파일의 끝이 올 것을 예상하지 못할 때 발생하는 오류

while True:
    try:
        print(input())
    except EOFError:
        break
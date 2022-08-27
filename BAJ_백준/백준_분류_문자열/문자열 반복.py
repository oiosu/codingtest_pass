# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성
# 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
# S에는 QR Code "alphanumeric" 문자만 들어있다.

import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\문자의 반복.txt", "r", encoding="utf-8")


# 1. R,S를 모두 문자열로 받아서 split()을 사용해 공백으로 구분해준다. (R은 나중에 int로 수정)

# 2. for j in S의 의미는 S문자열의 첫번째 인덱스부터 반복한다는 뜻.

# 3. end=''를 사용하면 옆으로 쭉 나열해서 출력시킴

# 4. print()를 사용해 다음줄에 커서 옮김


T=int(input())

for i in range(T):
    R,S=input().split()
    
    for j in S:
        print(j*int(R), end='')
    print()
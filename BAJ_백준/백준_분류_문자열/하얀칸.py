import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_문자열\하얀칸.txt", "r", encoding="utf-8")


chess = []
for _ in range(8):
    chess.append(list(map(str, list(input()))))

answer = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: #하얀칸일 경우
            if chess[i][j] == 'F': #F있을 경우
                answer += 1
print(answer)
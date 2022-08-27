#import sys
#sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2043.txt", "r", encoding = 'utf-8')

#주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각
# 예를 들어 비밀번호 P가 123 이고 주어지는 번호 K가 100 일 때, 100부터 123까지 
# 24번 확인하여 비밀번호를 맞출 수 있다.
# P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.

P, K = map(int, input().split())
print(abs(P-K) +1)

# P와 K를 입력받아 두 수의 차이를 구하고 1을 더한 값을 출력한다. 
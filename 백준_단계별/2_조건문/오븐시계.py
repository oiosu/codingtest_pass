# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 
# 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성
# 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력
# 단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 
# 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.


H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)


# C를 받아 시와 분으로 나눠 각각에 더해준다.
# 더한 결과 값으로 B(분) 값이 60이 넘어가면 A(시)에 1을 더해주고, B(분)에 60을 뺀다.
# 23시 59분에서 1분이 지나면 0시 0분이 되는 부분을 처리하기 위해 A(시)가 24와 같거나 커지면 24를 빼준다. 
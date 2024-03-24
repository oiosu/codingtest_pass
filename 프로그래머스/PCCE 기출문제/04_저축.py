# 문제설명 
# 진우는 돈을 모으기 위해 저축을 하려고 합니다. 목표로 하는 금액은 100만 원이며, 첫 달에 일정 금액을 넣은 뒤 70만 원까지는 
# 매월 조금씩 저축하다가 70만 원 이후부터는 월 저축량을 늘려 빠르게 목표 금액을 달성하고자 합니다.

# 첫 달에 저축하는 금액을 나타내는 정수 start, 
# 두 번째 달 부터 70만 원 이상 모일 때까지 매월 저축하는 금액을 나타내는 정수 before,
# 100만 원 이상 모일 때 까지 매월 저축하는 금액을 나타내는 정수 after가 주어질 때, 
# 100만 원 이상을 모을 때까지 걸리는 개월 수를 출력하도록 빈칸을 채워 코드를 완성해 주세요.


start = int(input())
before = int(input())
after = int(input())

money = start
month = 1 
while money < 70:
    money += before
    month += 1
while money < 100:
    money += after
    month += 1 
    
print(month)
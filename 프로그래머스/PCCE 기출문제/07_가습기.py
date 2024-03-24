# 문제 설명 
# 상우가 사용하는 가습기에는 "auto", "target", "minimum"의 세 가지 모드

# auto 모드 

    # 습도가 0 이상 10 미만인 경우 : 5단계
    # 습도가 10 이상 20 미만인 경우 : 4단계
    # 습도가 20 이상 30 미만인 경우 : 3단계
    # 습도가 30 이상 40 미만인 경우 : 2단계
    # 습도가 40 이상 50 미만인 경우 : 1단계
    # 습도가 50 이상인 경우 : 0단계

# target 모드 

    # 습도가 설정값 미만일 경우 : 3단계
    # 습도가 설정값 이상일 경우 : 1단계

# minimum 모드 

    # 습도가 설정값 미만일 경우 : 1단계
    # 습도가 설정값 이상일 경우 : 0단계
    

# 상우가 설정한 가습기의 모드 나타낸 문자열 mode_type
# 현재 공기 중 습도를 나타낸 정수 humidity
# 설정값을 나타낸 정수 val_set 
# 현재 가습기가 몇단계 작동 중인지 return 하기 


def func1(humidity, val_set):
    if humidity < val_set:
        return 3
    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    else:
     return 5

def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0

def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)

    elif mode_type == "target":
        answer = func1(humidity, val_set)

    elif mode_type == "minimum":
        answer = func3(humidity, val_set)

    return answer
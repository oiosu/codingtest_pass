# 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.

result = int(input())
if result % 400 == 0 and result % 100 != 0 :
    print('1')
elif result % 400 == 0 and result % 400 == 0:
    print('0')
else: 
    print('0')
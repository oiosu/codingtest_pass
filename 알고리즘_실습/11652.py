# 카드 
# 준규는 숫자 카드 N장을 가지고 있다. 
# 숫자 카드에는 정수가 하나 적혀있는데, 
# 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.
# 준규가 가지고 있는 카드가 주어졌을 때, 
# 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 
# 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

# 딕셔너리를 사용한 이유는 key값에 카드의 번호를 저장하고, 
# value값에 카드의 개수를 저장하여 마지막에 value값을 내림차순해주고 같다면 
# key값을 오름차순해주기 위해서이다.

import sys
input = sys.stdin.readline

n = int(input())
card_dic = {}

for i in range(n) :
    card = int(input())
    if card in card_dic :
        card_dic[card] += 1
    else :
        card_dic[card] = 1

result = sorted(card_dic.items(),key = lambda x : (-x[1],x[0]))
print(result[0][0])
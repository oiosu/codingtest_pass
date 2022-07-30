# 숫자 카드(2)

# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
# 상근이는 숫자 카드 N개를 가지고 있다. 
# 정수 M개가 주어졌을 때, 
# 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지?!

# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 
# 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 
# 구분해 출력한다.

#내장함수 
from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

count = Counter(card)

for i in range(len(test)):
    if test[i] in count:
        print(count[test[i]], end=' ')
    else:
        print(0, end=' ')



# 딕셔너리 
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

hash = {}

for i in card:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in test:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')
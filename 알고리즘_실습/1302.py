# 베스트셀러
# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 
# 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성
# input
# : 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 
# 이 값은 1,000보다 작거나 같은 자연수이다. 
# 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 
# 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.
# output
# : 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 
# 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 
# 가장 앞서는 제목을 출력


# keys에는 책 이름을, values에는 책이 나온 빈도를 저장
# 이후 최대 빈도를 찾아서 그 빈도와 같은 책 이름들만 저장하는 리스트 만들기
# 책 이름으로 정렬하고, 첫 번째 값을 출력

import sys
book = dict()
n = int(input())
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1
max = 0
sbook = dict(sorted(book.items()))
for i in sbook:
    if (sbook[i]) > max:
        max = sbook[i]
        maxi = i
print(maxi)
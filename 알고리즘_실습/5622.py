# 다이얼
# 숫자 1을 걸려면 총 2초가 필요하다.
# 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 
# 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 전화 번호를 각 숫자에 해당하는 문자로 외운다. 
# 예를 들어, UNUCIC는 868242와 같다. (대문자로 이루어진 단어)
# 할머니가 외운 단어가 주어졌을 때, 
# 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성


# 변수 apha을 소문자로 입력
alpha = input().lower() 
# 소문자 리스트
dial = ["abc", "def", "ghi", "jki", "mno", "pqrs", "tuv", "wxyz"] 
#필요한 시간을 알기위해 time이라는 변수에 0을 초기화 
time = 0 

# for문을 사용하여 입력받은 변수의 len 만큼 i를 반복 
for i in range(len(alpha)):
    # 이중 반복문을 통해 dial 에 있는 문자열 하나씩 j로 반복 
    for j in dial:
        if alpha[i] in j: #alpha이 j의 문자열에 해당된다면, 
            #time에 해당하는 dial의 index 수와 j가 0부터 반복하기 시작한
            # 것을 감안한 +3을 반복해서 더해준다. 
            time += dial.index(j) +3
print(time)



# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# ret = 0
# for j in range(len(a)):
#     for i in dial:
#         if a[j] in i:
#             ret += dial.index(i)+3
# print(ret)
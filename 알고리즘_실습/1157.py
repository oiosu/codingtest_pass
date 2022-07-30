# 가장 많이 사용된 알파벳
# 대소문자 상관 없음 
# 가장 많이 사용된 알파벳이 여러개 존재할 경우 ? 출력

# set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다. 
# 리스트에 포함된 요소 x의 개수 count
# 위치 반환 index

# 변수 word를 설정하고 lower()를 이용해서 입력받은 문자열을 대문자로 입력받고 
# set()을 사용하여 자료형의 중복을 제거한 뒤 list로!
word = input().upper() 
word_list = list(set(word)) 
# 가장 많이 사용된 알파벳을 알기 위한 cnt변수를 [] 리스트로 초기화 하기 
cnt = []

for i in word_list:  # i : M, I, S, P, / B, A 
    count = word.count(i)
    cnt.append(count(i)) # [4, 4, 1, 1] / [1, 3]
if cnt.count(max(cnt)) > 2:
        print("?")
else: 
    print(word_list[cnt.index(max(cnt))].upper())
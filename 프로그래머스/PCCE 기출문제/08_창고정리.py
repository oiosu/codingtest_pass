# 문제설명 

# 선빈이의 창고에 들어있는 물건의 이름과 개수는 리스트 형태로 주어지며 
# 한 칸에 겹쳐 질 수 있는 물건의 개수에는 제한이 없다고 가정 

# 창고의 각 칸에 담겨 있는 물건의 이름이 storage = ["pencil", "pencil", "pencil", "book"],
# 각 물건의 개수가 num = [2, 4, 3, 1] 이라면 
# 연필과 책을 한 칸에 각각 겹쳐 쌓아 간단하게 
# clean_storage = ["pencil", "book"], clean_num = [9, 1]로 만들 수 있다. 

# 주어진 solution 함수는 정리되기 전 창고의 물건 이름이 담긴 문자열 리스트 storage 와 
# 각 물건의 개수가 담긴 정수 리스트 num이 주어질 떄 정리도니 창고에서 개수가 가장 많은 물건의 
# 이름을 return 하는 함수 

def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            # clean_storage.append(num[i])
            clean_num.append(num[i])
    
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer
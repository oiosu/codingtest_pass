
def solution(data, ext, val_ext, sort_by):
    answer = []
    
    ext_dict = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}

    for d in data:
        if d[ext_dict[ext]] < val_ext:
            answer.append(d)

    answer.sort(key = lambda x: x[ext_dict[sort_by]])
    
    return answer


# 조건에 맞는 데이터를 추출한 후 오름차순으로 정렬하기 
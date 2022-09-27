T = int(input())

for i in range(T) :
    n = int(input())
    people_lst = [0]*n
    for j in range(n) :
            t1 ,t2 = map(int,input().split())
            people_lst[j] = [t1,t2]

    people_lst_sorted_0 = sorted(people_lst, key = lambda x : x[0])
    hired = 1
    for j in range(1,n) :
        num = 0
        for k in range(j) :
            if people_lst_sorted_0[j][1] < people_lst_sorted_0[k][1] :
                num += 1
            if num == j :
                hired += 1

    print(hired)
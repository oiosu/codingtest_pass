# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 
# 소수점 셋째 자리까지 출력

c=int(input())
for i in range(c): #(1)
    li=list(map(int,input().split()))
    c=0
    for j in li[1:]: #(2)
        avg=sum(li[1:])/li[0]
        if j>avg:
            c+=1
    rate=c/li[0]*100
    print('{0:0.3f}%'.format(rate))
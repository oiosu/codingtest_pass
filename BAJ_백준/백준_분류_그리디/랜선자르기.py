import sys
sys.stdin = open(r"C:\Users\LGD\Desktop\코딩테스트 합격\BAJ_백준\백준_분류_그리디\랜선자르기.txt", "r", encoding="utf-8")

k, n = map(int, input().split())
Line = []
res = 0
largest = 0

def Count(su):
    cnt = 0 
    for x in Line:
        cnt += (x//su)
    return cnt

for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

# 이분탐색
lt = 1
rt = largest
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid+1
        # 답이 아니였을 때 
    else:
        rt = mid-1
print(res)

# 끝 

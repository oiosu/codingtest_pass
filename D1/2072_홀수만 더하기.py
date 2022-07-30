import sys
sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2072.txt", "r", encoding = 'utf-8')


t = int(input())

for i in range(1, t + 1) :
    data = list(map(int, input().split()))
    result = 0
    for j in range(len(data)) :
        if data[j] % 2 == 1 :
            result += data[j]

    print('#%d %d' % (i, result))
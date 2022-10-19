n = int(input())
i = 0
cnt = 0
while True:
    if n > i: # n이 i보다 크면 n에 i를 차감
        i += 1
        n = n-i
        cnt += 1
    else:
        print(cnt)
        break

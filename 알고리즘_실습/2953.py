max_s = max_i = 0

for i in range(5):
    s = sum(map(int, input().split()))
    if s > max_s:
        max_s = s
        max_i = i+1
print(max_i, max_s)
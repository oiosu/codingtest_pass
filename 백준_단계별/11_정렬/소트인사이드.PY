nums = list(map(int, str(input())))
nums.sort(reverse=True)
for i in nums:
    print(i,end='')
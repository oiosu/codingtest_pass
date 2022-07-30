# import sys
# sys.stdin = open(r"C:\Users\LGE\Desktop\코딩테스트 합격\D1\2050.txt", "r", encoding = 'utf-8')


# t = int(input())
# month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# for i in range(1, t + 1) :
#     data = input()
#     result = [data[:4]]

#     if int(data[4:6]) in month :
#         result.append(data[4:6])
#     else :
#         print('#%d %d' % (i, -1))
#         continue

#     if 1 <= int(data[6:]) <= day[int(data[4:6])-1] :
#         result.append(data[6:])
#     else :
#         print('#%d %d' % (i, -1))
#         continue

#     print('#%d %s' % (i, "/".join(result)))
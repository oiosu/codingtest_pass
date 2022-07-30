result = list(map(int,input().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
dscending = [8, 7, 6, 5, 4, 3, 2, 1]

if result == ascending:
    print('ascending')
elif result  == dscending:
    print('dscending')
else: 
    print('mixied')

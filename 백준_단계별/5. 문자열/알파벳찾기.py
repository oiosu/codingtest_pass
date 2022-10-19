<<<<<<< HEAD
S = input()
check = [-1]*26
 
for i in range(len(S)):
    if check[ord(S[i])-97] != -1:
        continue
    else:
        check[ord(S[i])-97] = i
        
for i in range(26):
=======
S = input()
check = [-1]*26
 
for i in range(len(S)):
    if check[ord(S[i])-97] != -1:
        continue
    else:
        check[ord(S[i])-97] = i
        
for i in range(26):
>>>>>>> ffba77d72193687ce75e356a6d29096d959d5789
    print(check[i], end=' ')
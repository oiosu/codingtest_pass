<<<<<<< HEAD
t=int(input())

if t % 10 !=0:
    print(-1)
else:
    a,b,c=0,0,0
    a=t//300
    b=(t % 300) // 60
    c=(t % 60) // 10
=======
t=int(input())

if t % 10 !=0:
    print(-1)
else:
    a,b,c=0,0,0
    a=t//300
    b=(t % 300) // 60
    c=(t % 60) // 10
>>>>>>> ffba77d72193687ce75e356a6d29096d959d5789
    print(a,b,c)
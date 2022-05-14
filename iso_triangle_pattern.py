n=int(input())
i=1
while i<=n:
    space=1
    while space<=n-i:
        print(' ',end='')
        space=space+1
    star=1
    while star<=i:
        print('*',end='')
        star=star+1
    p=i-1
    while p>=1:
        print('*',end='')
        p=p-1
    print()
    i=i+1

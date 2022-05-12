#Write Your Code Here
n=int(input())
ldigit=0
if n==0:
    print(n)
else:
    while ldigit==0:
        ldigit=n%10
        n=n//10
    rnum=ldigit
    while n!=0:
        ldigit=n%10
        n=n//10
        rnum=(rnum*10)+ldigit
    print(rnum)

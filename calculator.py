# Write your code here
opnum=int(input())
while opnum!=6:
    if opnum==1:
        snum1=int(input())
        snum2=int(input())
        print(snum1+snum2)
    elif opnum==2:
        subnum1=int(input())
        subnum2=int(input())
        print(subnum1-subnum2)
    elif opnum==3:
        mnum1=int(input())
        mnum2=int(input())
        print(mnum1*mnum2)
    elif opnum==4:
        qnum1=int(input())
        qnum2=int(input())
        print(int(qnum1/qnum2))
    elif opnum==5:
        rnum1=int(input())
        rnum2=int(input())
        print(rnum1%rnum2)
    else:
        print("Invalid Operation")
    opnum=int(input())

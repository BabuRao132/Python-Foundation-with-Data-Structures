def checkPalindrome(num):
    n=num
#Implement Your Code Here

    ldigit=0
    if n//10<1:
        return True
    else:
        while ldigit==0:
            ldigit=n%10
            n=n//10
        rnum=ldigit
        while n!=0:
            ldigit=n%10
            n=n//10
            rnum=(rnum*10)+ldigit
    if rnum==num:
        return True

num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
    print('true')
else:
    print('false')

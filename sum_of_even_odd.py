## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
#Write Your Code Here
n=int(input())
val1=val2=0
while n!=0:
    ldigit=n%10
    n=n//10
    if ldigit%2==0:
        val1=val1+ldigit
    else:
        val2=val2+ldigit
print(val1," ",val2)

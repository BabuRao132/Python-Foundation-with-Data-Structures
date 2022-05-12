## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
x=0
y=1
i=1
while i<=n:
    if i==1:
        y=y
        i=i+1
    else:
        y=x+y
        x=y-x
        i=i+1
print(y)

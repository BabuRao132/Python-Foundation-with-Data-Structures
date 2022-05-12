# Read input as sepcified in the question
# Print output as specified in the question
s=int(input())
e=int(input())
w=int(input())
F=s
while F<=e:
    C=(F-32)*(5/9)
    print(F,int(C))
    F=F+w
